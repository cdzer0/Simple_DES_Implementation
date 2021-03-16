import DES

PlainTextList = ["May the Force be with you.",
                 "A census taker once tried to test me. I ate his liver with some fava beans and a nice Chianti.",
                 "You can't handle the truth!",
                 "Mama always said life was like a box of chocolates. You never know what you're gonna get.",
                 "Yo, Adrian!"]

def GenData():
    DES.KeyProNGen()
    one_time_key = DES.info['key']
    print('One time key is : ' + one_time_key + '\n')
    f = open('data.txt', 'w')
    for PT in PlainTextList:
        DES.info['PlainText'] = PT
        f.write(PT)
        f.write("\n")
        DES.Encrypt()
        f.write(DES.info['CipherText'])
        f.write("\n")
    f.close()

GenData()