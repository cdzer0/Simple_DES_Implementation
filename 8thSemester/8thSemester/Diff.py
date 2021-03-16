import DES
import All_Conversions as ac

P1 = "Hell"
P2 = "Helo"
P3 = "Help"
returned_pt_val = {}
returned_ct_val = {}
bin_pt_1 = ""
bin_pt_2 = ""
bin_pt_3 = ""
bin_ct_1 = ""
bin_ct_2 = ""
bin_ct_3 = ""
diff_P1P2 = ""
diff_P2P3 = ""
diff_P1P3 = ""
diff_C1C2 = ""
diff_C2C3 = ""
diff_C1C3 = ""

DES.KeyProNGen()
one_time_key = DES.info['key']
DES.info['PlainText'] = P1
DES.Encrypt()
DES.Decrypt()
bin_pt_1 = DES.info['PlainText_b']
C1 = DES.info['CipherText']
for i in C1:
    bin_ct_1 += ac.hex2bin(i)

DES.info['PlainText'] = P2
DES.Encrypt()
bin_pt_2 = DES.info['PlainText_b']
C2 = DES.info['CipherText']
for i in C2:
    bin_ct_2 += ac.hex2bin(i)

DES.info['PlainText'] = P3
DES.Encrypt()
bin_pt_3 = DES.info['PlainText_b']
C3 = DES.info['CipherText']
for i in C3:
    bin_ct_3 += ac.hex2bin(i)

for i in range(len(bin_pt_1)):
    diff_P1P2 += str(int(bin_pt_1[i]) ^ int(bin_pt_2[i]))
print("FROM DIFF DIFF_P1P2 IS ", diff_P1P2)

for i in range(len(bin_ct_1)):
    diff_C1C2 += str(int(bin_ct_1[i]) ^ int(bin_ct_2[i]))
print("FROM DIFF DIFF_C1C2 IS ", diff_C1C2)

for i in range(len(bin_pt_2)):
    diff_P2P3 += str(int(bin_pt_2[i]) ^ int(bin_pt_3[i]))
print("FROM DIFF DIFF_P2P3 IS ", diff_P2P3)

for i in range(len(bin_ct_2)):
    diff_C2C3 += str(int(bin_ct_2[i]) ^ int(bin_ct_3[i]))
print("FROM DIFF DIFF_C2C3 IS ", diff_C2C3)

for i in range(len(bin_pt_3)):
    diff_P1P3 += str(int(bin_pt_1[i]) ^ int(bin_pt_3[i]))
print("FROM DIFF DIFF_P1P3 IS ", diff_P1P3)

for i in range(len(bin_ct_3)):
    diff_C1C3 += str(int(bin_ct_1[i]) ^ int(bin_ct_3[i]))
print("FROM DIFF DIFF_C1C3 IS ", diff_C1C3)