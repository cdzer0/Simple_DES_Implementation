# Hexadecimal to binary conversion 
def hex2bin(s): 
	mp = {'0' : "0000", 
		'1' : "0001", 
		'2' : "0010", 
		'3' : "0011", 
		'4' : "0100", 
		'5' : "0101", 
		'6' : "0110", 
		'7' : "0111", 
		'8' : "1000", 
		'9' : "1001", 
		'a' : "1010", 
		'b' : "1011", 
		'c' : "1100", 
		'd' : "1101", 
		'e' : "1110", 
		'f' : "1111" } 
	bin = "" 
	for i in range(len(s)): 
		bin = bin + mp[s[i]] 
	return bin
	
# Binary to hexadecimal conversion 
def bin2hex(s): 
	mp = {"0000" : '0', 
		"0001" : '1', 
		"0010" : '2', 
		"0011" : '3', 
		"0100" : '4', 
		"0101" : '5', 
		"0110" : '6', 
		"0111" : '7', 
		"1000" : '8', 
		"1001" : '9', 
		"1010" : 'a', 
		"1011" : 'b', 
		"1100" : 'c', 
		"1101" : 'd', 
		"1110" : 'e', 
		"1111" : 'f' } 
	return mp[s]

# Binary to decimal conversion 
def bin2dec(binary): 
	binary1 = binary 
	decimal, i, n = 0, 0, 0
	while(binary != 0): 
		dec = binary % 10
		decimal = decimal + dec * pow(2, i) 
		binary = binary//10
		i += 1
	return decimal 

# Decimal to binary conversion 
def dec2bin(num): 
	res = bin(num).replace("0b", "") 
	if(len(res)%4 != 0): 
		div = len(res) / 4
		div = int(div) 
		counter =(4 * (div + 1)) - len(res) 
		for i in range(0, counter): 
			res = '0' + res 
	return res

def pt2hex(message, retdict):
	t1 = ""
	retdict["extra"] = 0
	if len(message) % 8 != 0:
		extra = 8 - len(message)%8
		retdict["extra"] = extra
		while extra:
			message += "0"
			extra -= 1
	for i in range(len(message)):
		num = ord(message[i])
		t1 += str(num) + " "
	#print(t1)
	t2 = ""
	pnum = ""
	for l in t1:
		if l == " ":
			num = dec2bin(int(pnum))
			pnum = ""
			t2 += str(num)
		else:
			pnum += l  
	#print(t2)
	retdict['b'] = t2
	t3 = ""
	for i in range(0,len(t2),4):
		ch = "" 
		ch = ch + t2[i] 
		ch = ch + t2[i + 1] 
		ch = ch + t2[i + 2] 
		ch = ch + t2[i + 3]
		t3 += bin2hex(ch)
	#print(t3)
	retdict['h'] = t3
