#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tools
from argparse import ArgumentParser



#Cesar's method
def cesar(string,key,decrypt):
    """
this is the fonction call by the main fonction for cesar cypher
    """
    if(type(key) is str) :
        key= ord(key[0])
    if (decrypt) :
        return cesarDecode(string,key)
    else :
        return cesarCode(string,key)

def cesarCode(string,key):
    res = ''
    for char in string :
    	res+=chr((ord(char)+key)%256)
    return res

def cesarDecode(string,key):
    res = ''
    for char in string :
    	res+=chr((ord(char)-key)%256)
    return res

#Vigenere's method
def vigCode(string,key) :
    """
    Code a message by using vigenere's method, the key must be an iterable
    """
    res=''
    length=len(key)
    i=0
    for char in string :
        res+=chr((ord(char)+key[i%length])%256)
        i+=1
    return res

def vigDecode(string,key) :
    """
    Decode a message by using vigenere's method, the key must be an iterable
    """
    res=''
    length=len(key)
    i=0
    for char in string :
        res+=chr((ord(char)-key[i%length])%256)
        i+=1
    return res


#Enigma's cipher method
def enigmaCode(string,key) :
    """
    Inspire by enigma ciphers (not sure if it's exactly the same)
    You need to use a bi-dimentional tab, the first dimension can be as long as you want and each tab on it is a ring of machin.
    The second dimention must contain 256 unique numbers between 0 and 255 (as much as the ASCII code).
    """
    res=''
    length=len(key)
    #construction of a int table, all at 0, representing the position of the rings
    i=[]
    for x in range (0, length) :
        i.append(0)
    #
    for char in string :
        temp=ord(char)
        for x in range (0, length) :
            temp=(key[x][(i[x]+temp)%256])
            #The ring is turnning one step ahead if it's the first ring
            #or if the previous ring make a complet turn
            if(x==0 or (i[x-1]!=0 and i[x-1]%256==0)):
                i[x]+=1
        res+=chr(temp)
    return res


def enigmaDecode(string,key) :
    """
    Use to decode a message using enigma cipher
    Inspire by enigma ciphers (not sure if it's exactly the same)
    You need to use a bi-dimentional tab, the first dimension can be as long as you want and each tab on it is a ring of machin.
    The second dimention must contain 256 unique numbers between 0 and 255 (as much as the ASCII code).
    """
    res=''
    length=len(key)
    #construction of a int table, all at 0, representing the position of the rings
    i=[]
    for x in range (0, length) :
        i.append(0)
    #
    for char in string :
        temp=ord(char)
        for x in range (length)[length::-1] :
            #The ring is turnning one step ahead if the previous ring make a complet turn
            if(x!=0 and i[x-1]!=0  and i[x-1]%256==0):
                i[x]+=1
            #searching the original value corresponding to result that we already have (temp)
            value = 0
            while (key[x][value]!=temp) :
                value+=1
            temp=(value-i[x])%256
            #The ring is turnning one step ahead if it's the first ring
            if(x==0 ):
                i[x]+=1
        res+=chr(temp)
    return res


#DES Cypher

#Initial permutation
PI= [58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8,57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7]
#inverse of the inital permutation
IP= [40,8,48,16,56,24,64,32,39,7,47,15,55,23,63,31,38,6,46,14,54,22,62,30,37,5,45,13,53,21,61,29,36,4,44,12,52,20,60,28,35,3,43,11,51,19,59,27,34,2,42,10,50,18,58,26,33,1,41,9,49,17,57,25]

E=[32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,12,13,12,13,14,15,16,17,16,17,18,19,20,21,20,21,22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1]

#The 8 S tables are put in one, the first index is for the number of the table 
S=[[[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],[0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],[4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],[15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]] , [[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],[3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],[0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],[13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]] , [[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],[13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],[13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],[1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]] , [[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],[13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],[10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],[3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]] , [[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],[14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],[4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],[11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]] , [[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],[10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],[9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],[4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]],[[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],[13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],[1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],[6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]] , [[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],[1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],[7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],[2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]]

#table for the last permutation 
FP=[16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25]

def DES(string,key,decrypt) : 
    """
Original DES (Data Encryption Standard), with the same weakness : a too short key
The string and the key are characters' strings, ideally the key must be 8 characters (more won't be use and with less the key is completed with empty space)
The third parameter is a boolean that tell if the algorithme crypt or decrypt the text, True is for decrypting.
    """
    lengthString = len(string)
    res=''
    #check if the key is from a correct longer and  add " " to this end if not
    lengthKey = len(key)
    while (lengthKey%8 != 0) :
        key+=(" ")
        lengthKey+=1
    #transform the key in a table of byte 
    keyB=[]
    for char in key : 
        for byte in ('{0:08b}'.format(ord(char))) : 
            keyB.append(int(byte))
    #contruction of the secondary keys
    keys = DESkeys(keyB)
    #change the order of the key if we want to decrypt
    if(decrypt):
        temp = keys[::-1]
        keys = temp
    # we need 64 bytes block,so if  we don't have a final block of 8 caracters, we complet it with  " " at the end of the String
    while (lengthString%8 != 0) :
        string+=(" ")
        lengthString+=1
    #
    for i in range(lengthString/8) :
        #char are converted in binairy
        init=''
        for j in range(8) :
            init+='{0:08b}'.format(ord(string[i*8+j]))
        #first permutation and splitting in 2 tabs of bytes
        L=[]
        R=[]
        for j in range(32) :
            L.append(int(init[PI[j]-1]))
        for j in range(32,64) :
            R.append(int(init[PI[j]-1]))
        #now application of the feistel's scheme with 16 round
        Rres=[]
        Lres=[]
        (Lres,Rres)=feistelCypher(L,R,16,keys)
        #now that 8 characters have been cypher we apply the inverse of the initial permutation
        L=Rres[:]
        L.extend(Lres)
        finalTab=[]
        for j in range(64) :
            finalTab.append(int(L[IP[j]-1]))
        #we convert the byte in char
        for j in range(8) :
            res+=chr((finalTab[j*8]*128+finalTab[j*8+1]*64+finalTab[j*8+2]*32+finalTab[j*8+3]*16+finalTab[j*8+4]*8+finalTab[j*8+5]*4+finalTab[j*8+6]*2+finalTab[j*8+7])%256)
    return res


def DESsimple(string,key,decrypt, nb) : 
    """
Simplified version using lists of bytes for the message and the key and returning a bytes' list, you can choose the number of round the feistal scheme will be apply
    """
    res=''
    lengthString=len(string)
    #check if the key is from a correct longer and  add " " to this end if not
    if (len(key)!=64) :
        print 'The key\'s longer is not good'
    #contruction of the secondary keys
    keys = DESkeys(key)
    if(decrypt):
            temp = keys[::-1]
            keys = temp           
    for i in range(lengthString/64) :
        #first permutation and splitting in 2 tabs of bytes
        L=[]
        R=[]
        for j in range(32) :
            L.append(string[PI[j]-1])
        for j in range(32,64) :
            R.append(string[PI[j]-1])
        #now application of the feistel's scheme
        Rres=[]
        Lres=[]
        (Lres,Rres)=feistelCypher(L,R,16,keys)
        #now that 8 characters have been cypher we apply the inverse of the initial permutation
        L=Rres[:]
        L.extend(Lres)
        finalTab=[]
        for j in range(64) :
            finalTab.append(int(L[IP[j]-1]))
    return finalTab


#The fonction is use to create the secondary key from primary key (for DES cypher)

#First permutation table
PC1 = [57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]

#
PC2 = [14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2,41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]

def DESkeys(primKey) :
    """
Take a primary key and create 16 secondary keys for the DES algo, the key must be a table of bytes.
This version is for a 64 bytes key (event if the security is like a 56 bytes key)
    """
    key=[] #the table contaning the 16 keys
    #first permutation and splitting in 2 tabs of bytes
    U=[]
    D=[]
    for i in range(28) :
        U.append(primKey[PC1[i]-1])
    for i in range(28,56) :
        D.append(primKey[PC1[i]-1])
    #creation of the 16 sub keys 
    for i in range(16) :
        #the left rotation 
        if (i==0 or i==1 or i==8 or i==15) :
            temp=U[0]
            for j in range(27):
                U[j]=U[j+1]
            U[27]=temp
            temp=D[0]
            for j in range(27):
                D[j]=D[j+1]
            D[27]=temp
        else :
            temp1=U[0]
            temp2=U[1]
            for j in range(26):
                U[j]=U[j+2]
            U[26]=temp1
            U[27]=temp2
            temp1=D[0]
            temp2=D[1]
            for j in range(26):
                D[j]=D[j+2]
            D[26]=temp1
            D[27]=temp2
        #put back the two table together and apply PC2 to have a secondary key
        temp=[x for x in U]
        temp+=[x for x in D]
        key.append([])
        key[i]=[temp[PC2[x]-1] for x in range(48)]
    #finaly we return the keys
    return key


def feistelCypher(left,right, roundNb, keys):
    """
For now the fonction used is the one in DES, but it's planned to be usable with any given fonction.
the nomber of round use in this algorithm
    """
    length = len(left)
    for i in range (roundNb):
        #first we get the result of f(right,Key)
        #here for DES : 
        ##expension
        afterE=[right[x-1] for x in E]
        ##add of the key
        afterKey=[ (afterE[x]+keys[i][x])%2  for x in range(48) ]
        ##now we use the S boxes
        afterS=[]
        for j in range (8) : 
            #HERE THERE IS 2 different way to find the value give by Sj
            x=afterKey[j*6]*2+afterKey[j*6+5]
            y=afterKey[j*6+1]*8+afterKey[j*6+2]*4+afterKey[j*6+3]*2+afterKey[j*6+4]
            value = S[j][x][y]
            for byte in '{0:04b}'.format(value):
                afterS.append(int(byte))
        ## now we apply a final permutation to have the result of the fj fonction
        f = [ afterS[x-1] for x in FP ]
        #add of the fonction and the left part to have the new rigth part
        rightNext = [ (left[x]+f[x])%2 for x in range (length) ]
        #
        left=right[:]
        right=rightNext[:]
    # at the end we return the left and the right parts
    return (left, right)

#TDES triple DES

def TDES(message, keys, decrypt) :
    """
TDES (Triple DES) is a safer cypher algorithm than the DES, because the key longer is long enough (still 128 bytes event with a middle attack technics). But not as good as AES in term of execution time.
Keys must be a tuple of 3 keys, each one containing 8 characters
    """
    res=''
    #transform the keys in a tables of byte 
    keysB=[[],[],[]]
    for i in range(3) :
        for char in keys[i] : 
            for byte in ('{0:08b}'.format(ord(char))) : 
                keysB[i].append(int(byte))
    if(decrypt):
        temp = keysB[0][:]
        keysB[0] = keysB[2][:]
        keysB[2] = temp
   
    #add characters in the end in case it's not a multiple of 8
    charToAdd = (len(message))%8
    while (charToAdd > 0) :
        message+=(' ')
        charToAdd-=1
    #tranform the characters in bytes 
    messB=[]
    for char in message : 
        for byte in ('{0:08b}'.format(ord(char))) : 
            messB.append(int(byte))
    #DESsimple is just working with block of 64 bytes so we cut the message
    for i in range(len(messB)/64):
        #apply 3 times the DES
        inter1 = DESsimple(messB[i*64:i*64+64],keysB[0],decrypt,16)
        inter2 = DESsimple(inter1,keysB[1], not decrypt,16)
        resB = DESsimple(inter2,keysB[2],decrypt,16)
        #tranform the result in bytes to a result in characters
        for j in range(8):
            res+=chr((resB[j*8]*128+resB[j*8+1]*64+resB[j*8+2]*32+resB[j*8+3]*16+resB[j*8+4]*8+resB[j*8+5]*4+resB[j*8+6]*2+resB[j*8+7])%256)
    return res


#RSA 

def RSAsimple (message, n, key) :
    """
A basic version of the RSA cypher that isn't optimal in term of algorithm complexity.
This algorithm complexity is exponential with n value.
The message must be an integer.
    """
    return ((message)**key)%n


def RSAint (message, n, key) :
    """
A version working with bytes.
Not sure if it so much better in term of complexity in python, but theoretically the complexity is polynomial with the key's length (in bytes).
    """
    #transfor the key in a byte string
    keyTab=[int(byte) for byte in ('{0:0b}'.format(key))][::-1]
    length = len(keyTab)
    y=[message,]
    for i in range(1, length) :
        y.append((y[i-1]**2)%n)
    #caculation of the result
    result = 1
    for i in range(length):
        if keyTab[i] :
            result*=y[i]
    return result%n     

def RSAstring (message, n, key, decrypt):
    """
The value of n must be bigger than 255. And it can't be pair (which won't be probably).
    """
    res = ''
    #first we find the length of the blocks we're gonna use
    #length is the number of characters in one block for the message, the number of characters in a crypted block is one character longer than in clear
    length = 1
    while (256**length<n) :
        length+=1
    length-=1
    lengthA = length +1
    if (decrypt) :
        length+=1
        lengthA-=1
    while (len(message)%length != 0): #check if there is enough characters is the last block
        message+=' '
    for i in range (len(message)/length):
        #put the block chars into a tab of bytes
        bytes = []
        for j in range (length) :
            bytes.extend([int(byte) for byte in ('{0:08b}'.format(ord(message[j+i*length])))][::-1])
        # transforme the tab of bytes into an interger
        value = bytes[0]
        for j in range (1,len(bytes)) :
            value += (bytes[j]*2)**j
        #now application of the RSA cypher
        resultInt = RSAint(value, n, key)
        # translate the value in bytes
        resB = [int(byte) for byte in '{0:0b}'.format(resultInt)][::-1]
        while (len(resB)<lengthA*8) :
            resB.append(0)
        #transfomation in char
        for j in range (lengthA) :
            val=((resB[j*8]+resB[j*8+1]*2+resB[j*8+2]*4+resB[j*8+3]*8+resB[j*8+4]*16+resB[j*8+5]*32+resB[j*8+6]*64+resB[j*8+7]*128))
            res+=chr(val)
    return res

def RSA (message, n, key, decrypt) :
    """
    """
    #Sadly there is no surchage in python, that's the raison this fonction exist
    if (type(message) == str) :
        return RSAstring(message, n, key, decrypt)
    elif (type(message) == int) :
        return RSAint(message, n, key)     
    else :
        return 0
        #raise an exception

# lunch when use as a script
def main():
    parser = ArgumentParser( description="""This is a cypher tool from ASCII characters to ASCII characters, exemple of use : ./code -a DES -k exempKey <clear.txt > crypted.txt""")
    parser.add_argument ("-d", "--decrypt", dest='decrypt', default=False, action='store_true', help="decrypt message instead of encrytping it")
    parser.add_argument ("-k", "--key", dest='key', default='0', action='store', help='the key use by the cypher algorithm')
    parser.add_argument ("-a", "--algo", dest='algo', default='DES', action='store', help='algorithm use for crypt or decrypt, available algorithms are DES and RSA')
    parser.add_argument ("-n", "--modulus", dest='n', action='store', help='cipher modulus for RSA')
    args = parser.parse_args()
    message = raw_input()
    #switch 
    if(args.algo=='DES'):
        result = DES(message, args.key, args.decrypt)
    elif(args.algo=='RSA'):
        result = RSA(message, int(args.n), int(args.key), args.decrypt)
    else :
        result = cesar(message, args.key, args.decrypt)
    print result


if __name__ == '__main__':
    exit(main())
