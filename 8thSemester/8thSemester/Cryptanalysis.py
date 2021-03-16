import DES

f = open('data.txt', 'r')
CTList = []
PTList = []
for i in range(5):
    PT = f.readline()
    PTList.append(PT.replace('\n',''))
    CT = f.readline()
    CTList.append(CT.replace('\n',''))
f.close()
for i in range(5):
    print(PTList[i], " Corresponds to ", CTList[i], "\n")