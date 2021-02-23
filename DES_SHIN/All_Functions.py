import All_Conversions as ac
import random

# Random Key Generation
def GenerateKey():
    key_base = "0123456789abcdef"
    key = ""
    for i in range(16):
        key += random.choice(key_base)
    return key

# Key Initial Permutation 1 
IP1 = [56, 48, 40, 32, 24, 16, 8, 0, 57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 60, 52, 44, 36, 28, 20, 12, 4, 27, 19, 11, 3]
def permuteOne(k): 
    permutation = "" 
    for i in range(56): 
        permutation = permutation + k[IP1[i]] 
    return permutation

# Key Initial Permutation 2
IP2 = [13, 16, 10, 23, 0, 4, 2, 27, 14, 5, 20, 9, 22, 18, 11, 3, 25, 7, 15, 6, 26, 19, 12, 1, 40, 51, 30, 36, 46, 54, 29, 39, 50, 44, 32, 47, 43, 48, 38, 55, 33, 52, 45, 41, 49, 35, 28, 31]
def keyRotationNpermuteTwo(k,i,retdict):
    round_shift = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    l_k = ""
    r_k = ""
    lcs_key = ""
    permutation = ""
    for m in range(round_shift[i],28):
        l_k += k[m]
    for n in range(0,round_shift[i]):
        l_k += k[n]
    #print("l_k for " + str(i + 1) + " is " + l_k)
    for m in range(28+round_shift[i],56):
        r_k += k[m]
    for n in range(28,28+round_shift[i]):
        r_k += k[n]
    #print("r_k for " + str(i + 1) + " is " + r_k)
    # l_k = k[round_shift[i]:28] + k[:round_shift[i]]
    # r_k = k[28 + round_shift[i]:] + k[28:28+round_shift[i]]
    for l in range(56):
        if l<28:
            lcs_key += l_k[l]
        else:
            lcs_key += r_k[l-28]
    #print("lcs_key for " + str(i + 1) + " is " + lcs_key)
    retdict["lcs_key"] = lcs_key
    for j in range(48):
        permutation = permutation + lcs_key[IP2[j]]
    retdict["p2key"] = permutation
    #print("p2key for " + str(i + 1) + " is " + retdict["p2key"] + "\n")

# Initial Permutatiton Function
IPfirst = [57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7, 56, 48, 40, 32, 24, 16, 8, 0, 58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6]
def permuteThree(pt_block):
    pt_block_str = ""
    for i in range(64):
       pt_block_str += pt_block[IPfirst[i]]
    return pt_block_str

IPLast = [15, 6, 19, 20, 28, 11, 27, 16, 0, 14, 22, 25, 4, 17, 30, 9, 1, 7, 23, 13, 31, 26, 2, 8, 18, 12, 29, 5, 21, 10, 3, 24] 
def permuteFour(s_box_res):
    p_s_box_res = ""
    for i in range(32):
       p_s_box_res += s_box_res[IPLast[i]]
    return p_s_box_res

IPinv = [39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29, 36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25, 32, 0, 40, 8, 48, 16, 56, 24] 
def permuteFive(final_block_str):
    inv_final_block_str = ""
    for i in range(64):
        inv_final_block_str += final_block_str[IPinv[i]]
    return inv_final_block_str

def Expansion(r_block_str):
    exp_r_block_str = ""
    exp_one=[31,3,7,11,15,19,23,27]
    exp_two=[4,8,12,16,20,24,28,0]
    j = 0
    k = 0
    l = 0
    for i in range(48):
        if i%6==0:
            exp_r_block_str += r_block_str[exp_one[j]]
            j+=1
        elif i%6==5:
            exp_r_block_str += r_block_str[exp_two[k]]
            k+=1
        else:
            exp_r_block_str += r_block_str[l]
            l+=1
    return exp_r_block_str

sbox = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7], 
        [ 0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8], 
        [ 4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0], 
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13 ]], 
            
        [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10], 
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5], 
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15], 
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9 ]], 
    
        [ [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8], 
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1], 
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7], 
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12 ]], 
        
        [ [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15], 
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9], 
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4], 
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14] ], 
        
        [ [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9], 
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6], 
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14], 
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3 ]], 
        
        [ [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11], 
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8], 
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6], 
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13] ], 
        
        [ [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1], 
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6], 
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2], 
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12] ], 
        
        [ [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7], 
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2], 
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8], 
            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11] ] ] 

def encrypt(block_str, p2key, test_returned_block_val):
    l_block_str = ""
    r_block_str = ""
    exp_r_block_str = ""
    res_r_block_xor_p2key = ""
    res_s_box = ""
    final_r_block = ""
    final_l_block = ""
    
    for i in range(32):
        l_block_str += block_str[i]
    #print("l_block_str is : " + l_block_str)
    for i in range(32):
        r_block_str += block_str[i+32]
    #print("r_block_str is : " + r_block_str)

    exp_r_block_str = Expansion(r_block_str)
    #print("exp_r_block_str is : " + exp_r_block_str)
    
    for i in range(48):
        res_r_block_xor_p2key += str(int(exp_r_block_str[i]) ^ int(p2key[i]))
    #print("res_r_block_xor_p2key is : " + res_r_block_xor_p2key)

    for i in range(0,48,6):
        row = int(res_r_block_xor_p2key[i])*2 + int(res_r_block_xor_p2key[i+5])*1
        col = int(res_r_block_xor_p2key[i+1])*8 + int(res_r_block_xor_p2key[i+2])*4 + int(res_r_block_xor_p2key[i+3])*2 + int(res_r_block_xor_p2key[i+4])*1
        #print("Row is : " + str(row) + " Col is : " + str(col) + " and number at " + str(int(i/6)) + " is : " + str(sbox[int(i/6)][row][col]))
        bin_num = ac.dec2bin((sbox[int(i/6)][row][col]))
        #print("Bin Number is : " + str(bin_num))
        res_s_box += str(bin_num)
    #print("res_s_box is : " + res_s_box)

    p_s_box_res = permuteFour(res_s_box)
    #print("p_s_box_res is " + str(p_s_box_res))

    for i in range(32):
        final_r_block += str(int(p_s_box_res[i]) ^ int(l_block_str[i]))
    #print("final_r_block is : " + final_r_block)
    final_l_block = r_block_str
    #print("final_l_block is : " + final_l_block)
    test_returned_block_val['l'] = final_l_block
    test_returned_block_val['r'] = final_r_block

# ******** TESTING FOR BLOCK ******** #
# K1 = "000110110000001011101111111111000111000001110010"
# R0 = "11110000101010101111000010101010"
# IP = "1100110000000000110011001111111111110000101010101111000010101010"
# a = ""
# b = ""
# encrypt(IP, K1, a, b)
