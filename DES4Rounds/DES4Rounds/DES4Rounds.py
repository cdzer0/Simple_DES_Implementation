import All_Conversions as ac
import All_Functions as af

info = {}
key_dict = {}

def KeyProNGen():
    #key = "e1287a90b6cf35d4"
    key = "133457799bbcdff1"
    print('Key is : ' + key + '\n')
    info['key'] = key # For the duration of testing period only, since for cryptanalysis, direct access of "info['key']" should be restricted
    returned_key_val = {}
    bin_key = ac.hex2bin(key)
    p1key = af.permuteOne(bin_key) # 64-bit -> 56-bit key
    for q in range(4):
        af.keyRotationNpermuteTwo(p1key,q,returned_key_val) 
        p1key = returned_key_val["lcs_key"]
        key_dict[q] =  returned_key_val["p2key"]

KeyProNGen()
for i in range(4):
    print("Round ", i, " Key is : ", key_dict[i])

def Encrypt():
    
    returned_block_val = {}

    info['PlainText'] = "Superman"
    returned_pt_val = {}
    ac.pt2hex(info['PlainText'], returned_pt_val)
    print("Binary is ", returned_pt_val['b'])
    print(len(returned_pt_val['b']))
    #print("Hex is ", returned_pt_val['h'])

    CipherText = ""

    block_str = af.permuteThree(returned_pt_val['b'])
    for i in range(4):
        af.encrypt(block_str, key_dict[i], returned_block_val)

        block_str = returned_block_val['l'] + returned_block_val['r']
            
        print("block_str is : ",block_str," of length ", len(block_str))
        print("final_r_block is : " + returned_block_val['r'])
        print("final_l_block is : " + returned_block_val['l'])
        print("#ROUND " + str(i+1) + " Ended. \n")

    final_block_str = returned_block_val['r'] + returned_block_val['l']

    print("final_block_str is : " + final_block_str)
        
    inv_final_block_str = af.permuteFive(final_block_str)
        
    print("inv_final_block_str is : " + inv_final_block_str)
        
    for i in range(0,len(inv_final_block_str),4):
        ch = "" 
        ch = ch + inv_final_block_str[i] 
        ch = ch + inv_final_block_str[i + 1] 
        ch = ch + inv_final_block_str[i + 2] 
        ch = ch + inv_final_block_str[i + 3]
        CipherText = ac.bin2hex(ch)
    print("\nCipherText is : " + CipherText + "\n")
    info['CipherText'] = CipherText

Encrypt()

def Decrypt():
    pass

