import math
import os
path = r"/Users/Ryan/Documents/Encrypt.enc" #input("Input the path")

numline = input("Input two digit numbers")

file = open(path)

out= path[0:len(path)-3] + "enc"
#print(out)

message = file.read()
#print (message)
cipher = []
hold = []

numlist = []

numlist = numline.split(" ")


#print(numlist)

keylist = [0,1,2,3,4,5,6,7,8,9]
index = 0
for number in numlist:

    ind1 =  int (number[0])
    ind2 =  int (number[1])
    #print(ind1,ind2)
    keylist[ind1], keylist[ind2] = keylist[ind2], keylist[ind1]

print ("keylist", keylist)





for letter in message:
    hold.append(format(ord(letter), '#010b'))
   #hold.append(bin(ord(letter)))
   #print ("ord: ", bin(ord(letter)))


#print (hold[:])

outlist = [[],[],[],[],[],[],[],[],[],[]]

ind = 0

for bit in hold:
    #print(bit)
    col = ind % 10
    #print("col: ",col)
    outlist[col].append(bit)
    print("col", col, "bit", (chr(int(bit,2))))
    ind += 1
print ("outlist: ", outlist)
(votes[index][0])
'''for num in keylist:
    keyind = num
    print("keyind: ", keyind)
    cipher.extend((outlist[num]))
print("cipher  : ",cipher[:])

for i in range(0,len(cipher[:])):
    cipher[i]= chr(int(cipher[i],2))
    print(cipher[i])

print ("cipher list: ",cipher)
'''
plaintxt = []
print("len", len(message)-1)
for index in range(0,len(message)):

    row = index // 10
    #print("row",row)
    col = keylist[index % 10]
    print("col",col)
    print((chr(int(outlist[col][row],2))))
print("plaintext", plaintxt[:])


#outfile = open(out,'w')

#outfile.write(''.join(cipher))