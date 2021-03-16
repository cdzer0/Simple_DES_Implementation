# ******** TESTING FOR 4 ROUND DES - FAILED ******** #
#import DES_4R

#DES_4R.KeyProNGen()
#one_time_key = DES_4R.info['key']
#print('One time key is : ' + one_time_key + '\n')
#DES_4R.info['PlainText'] = "Hell"
#DES_4R.Encrypt(0,8)
#DES_4R.Decrypt(0,8)
## 1,1,2,2,2,2,2,2 - Round Shift for 8 round DES encryption
## 14,2,2,2,2,2,2,1 - Round Shift for 8 round DES decryption

# ******** TESTING FOR INDIVIDUAL FUNCTIONS IN DES ******** #
# def Testing():
#     # ******** TESTING FOR KEY ******** #
#     test_bin_key = "0001001100110100010101110111100110011011101111001101111111110001"
#     p1key = af.permuteOne(test_bin_key) # 64-bit -> 56-bit key
#     print("p1key is : " + p1key + " Its length is " + str(len(p1key)))
#     for i in range(16):
#         print("Key for round " + str(i) + " is : " +  key_dict[i])

#     # ******** TESTING FOR BLOCK ******** #
#     test_block = "0000000100100011010001010110011110001001101010111100110111101111"
#     test_block_list = test_block[:]
#     test_block_str = af.permuteThree(test_block_list)
#     print("Final Message is " + test_block_str)
#     # R0 = "11110000101010101111000010101010"
#     # IP = "1100110000000000110011001111111111110000101010101111000010101010"
#     test_returned_block_val = {}
#     final_test_block_str = ""
#     inv_final_test_block_str = ""
#     for j in range(16):
#         print("#ROUND " + str(j+1) + " : ")
#         af.keyRotationNpermuteTwo(p1key,j,returned_key_val) 
#         p1key = returned_key_val["lcs_key"]
#         print("p1key is : " + p1key + " Its length is " + str(len(p1key)))
#         key_dict[j] =  returned_key_val["p2key"]

#         af.encrypt(test_block_str, returned_key_val["p2key"],test_returned_block_val)
#         test_block_str = test_returned_block_val['l'] + test_returned_block_val['r']
#         print("test_block_str is : " + test_block_str)
#         print("final_r_block is : " + test_returned_block_val['r'])
#         print("final_l_block is : " + test_returned_block_val['l'])
#         print("#ROUND " + str(j+1) + " Ended. \n")

#     final_test_block_str = test_returned_block_val['r'] + test_returned_block_val['l']
#     print("final_test_block_str is : " + final_test_block_str)
#     inv_final_test_block_str = af.permuteFive(final_test_block_str)
#     print("inv_final_test_block_str is : " + inv_final_test_block_str)

#     CT = ""
#     for i in range(0,len(inv_final_test_block_str),4):
#         ch = "" 
#         ch = ch + inv_final_test_block_str[i] 
#         ch = ch + inv_final_test_block_str[i + 1] 
#         ch = ch + inv_final_test_block_str[i + 2] 
#         ch = ch + inv_final_test_block_str[i + 3]
#         CT += ac.bin2hex(ch)
#     print("CT is : " + CT)
# Testing()