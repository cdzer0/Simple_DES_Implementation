import All_Conversions as ac
import All_Functions as af

info = {}
key_dict = {}
#key = "e1287a90b6cf35d4" #Some hex value

def KeyProNGen():
    key = af.GenerateKey()
    #print('Key is : ' + key + '\n')
    info['key'] = key # For the duration of testing period only, since for cryptanalysis, direct access of "info['key']" should be restricted
    print("One time key is ", info['key'])
    returned_key_val = {}
    bin_key = ac.hex2bin(key)
    p1key = af.permuteOne(bin_key) # 64-bit -> 56-bit key
    for q in range(16):
        af.keyRotationNpermuteTwo(p1key,q,returned_key_val) 
        p1key = returned_key_val["lcs_key"]
        key_dict[q] =  returned_key_val["p2key"]
#******** FUNCTION CALL ********#
#KeyProNGen()

#******** ENCRYPTION ********#
def Encrypt():
    returned_pt_val = {}
    returned_block_val = {}

    #******** START OF ENCRYPTION ********#
    ac.pt2hex(info['PlainText'], returned_pt_val)
    
    print("Plaintext in binary is : ", returned_pt_val['b'],"\n")
    info['PlainText_b'] = returned_pt_val['b']

    info['extra'] = returned_pt_val['extra']
    CipherText = ""
    for i in range(0, len(returned_pt_val['b']), 64):
        block = returned_pt_val['b'][i:i+64]

        print("Block " + str(int(i/64) + 1) + " is : " + block)
        
        block_str = af.permuteThree(block)
        final_block_str = ""
        inv_final_block_str = ""

        #******** START OF ROUNDS ON EACH BLOCK ********#
        for j in range(16):
            af.encrypt(block_str, key_dict[j], returned_block_val)
            block_str = returned_block_val['l'] + returned_block_val['r']
            
            print("block_str is : " + block_str)
            print("final_r_block is : " + returned_block_val['r'])
            print("final_l_block is : " + returned_block_val['l'])
            print("#ROUND " + str(j+1) + " Ended. \n")

        final_block_str = returned_block_val['r'] + returned_block_val['l']

        print("final_block_str is : " + final_block_str)
        
        inv_final_block_str = af.permuteFive(final_block_str)
        
        print("inv_final_block_str is : " + inv_final_block_str)
        
        CT = ""
        for i in range(0,len(inv_final_block_str),4):
            ch = "" 
            ch = ch + inv_final_block_str[i] 
            ch = ch + inv_final_block_str[i + 1] 
            ch = ch + inv_final_block_str[i + 2] 
            ch = ch + inv_final_block_str[i + 3]
            CT += ac.bin2hex(ch)
        #print("CT for " + inv_final_block_str + " is : " + CT + "\n")
        CipherText += CT
    print("\nCipherText is : " + CipherText + "\n")
    info['CipherText'] = CipherText
##******** FUNCTION CALL ********#
#Encrypt()

#******** DECRYPTION ********#
def Decrypt():
    d_returned_block_val = {}
    d_block = ""
    RPlainText = ""

    #******** START OF DECRYPTION ********#
    for i in range(0, len(info['CipherText']), 16):
        d_block = info['CipherText'][i:i+16]

        print("D_Block " + str(int(i/16) + 1) + " is : " + d_block)
        
        bin_d_block = ""
        for i in range(len(d_block)):
            bin_d_block += ac.hex2bin(d_block[i])

        # print("bin_d_block for D_Block " + d_block + " is : " + bin_d_block)
        
        bin_d_block_str = af.permuteThree(bin_d_block)
        
        #print("bin_d_block_str is : " + bin_d_block_str)
        
        d_final_block_str = ""
        d_inv_final_block_str = ""

        #******** START OF ROUNDS ON EACH BIN_D_BLOCK ********#
        for j in range(16):
            af.encrypt(bin_d_block_str, key_dict[15-j], d_returned_block_val) # d_returned_key_val["p2key"]
            bin_d_block_str = d_returned_block_val['l'] + d_returned_block_val['r']
            
            print("bin_d_block_str is : " + bin_d_block_str)
            print("d_final_r_block is : " + d_returned_block_val['r'])
            print("d_final_l_block is : " + d_returned_block_val['l'])
            print("#ROUND " + str(j+1) + " Ended. \n")

        d_final_block_str = d_returned_block_val['r'] + d_returned_block_val['l']
        
        print("d_final_block_str is : " + d_final_block_str)
        
        d_inv_final_block_str = af.permuteFive(d_final_block_str)
        
        print("d_inv_final_block_str is : " + d_inv_final_block_str)

        PT = ""
        for a in range(0,len(d_inv_final_block_str),8):
            ch = d_inv_final_block_str[a:a+8]
            num = ac.bin2dec(int(ch))
            PT += chr(num)
        # print("PT for " + d_inv_final_block_str + " is : " + PT + "\n")
        RPlainText += PT
    RPlainText = RPlainText[:len(RPlainText)-info['extra']]
    print("Recovered PlainText is : " + RPlainText + "\n")
##******** FUNCTION CALL ********#
#Decrypt()

def SingleUser():
    KeyProNGen()
    PT = input("Enter a PlainText")
    info['PlainText'] = PT
    print('PlainText is : ', info['PlainText'])
    Encrypt()
    Decrypt()
##******** FUNCTION CALL ********#
#SingleUser()