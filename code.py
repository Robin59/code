#!/usr/bin/env python

import tools

#Cesar's method
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

PI= [58,50,40,42,34,26,18,10,2,60,52,44,36,28,20,12,4,62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8,57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7]

E=[32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,12,13,12,13,14,15,16,17,16,17,18,19,20,21,20,21,22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1]

#The 8 S tables are put in one, the first index is for the number of the table 
S=[[[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],[0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],[4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],[15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]],[[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],[3,13,4,7,15,2,8,14,13,0,1,10,6,9,11,5],[0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],[13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]],[[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],[13,7,0,9,3,4,9,8,15,3,0,11,1,2,12,5,10,14,7],[1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]],[[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],[13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],[10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],[3,15,0,6,10,1,3,8,9,4,5,11,12,14]],[[]]]#missing S5 to S8, bug with S3 and S4

#table for the last permutation 
FP=[16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25]

def DEScode(string,key) : 
    lengthString = len(string)
    # we need 64 bytes block,so if  we don't have a final block of 8 caracters, we complet it with  " " at the end of the String
    while (lengthString%8 != 0) :
        string+=(" ")
        lengthString+=1
    
    for i in range(lengthString/8) :
        #char are converted in binairy
        init=''
        for j in range(8) :
            init+='{0:08b}'.format(ord(string[i*8+j]))
        #first permutation and splitting in 2 tabs of bytes
        L=[]
        R=[]
        for j in range(32) :
            L.append(init[PI[j]-1])
        for j in range(32,64) :
            R.append(init[PI[j]-1])
        #now we're gonna do 16 permutations and transformations with 16 different keys on this blocks
        for j in range(16) :
            Rnext=[]#this is Rn+1 the result of the permutation and transformation
            #expension fonction E on the left part L
            temp=[]
            for l in E :
                temp.append(L[l-1])
            #tranformation with the key
            mockKey=[0 for x in range(48)] #a mock key that don't do anything
            temp2=[(int(temp[x])+mockKey[x])%2 for x in range (48)]
            #back to a new tab with 32 elements by using the tabs S
            temp3=[]
            for l in range(8) :
                #searching the coresponding value in the Sx table
                x=temp2[l*6]*2+temp2[l*6+5]
                y=temp2[l*6+1]*8+temp2[l*6+2]*4+temp2[l*6+3]*2+temp2[l*6+4]
                value = S[l][x][y]
                #tranform this value in bytes and put them in the new table with 32 cases
                for byte in '{0:08b}'.format(value):
                    temp3.append(byte)
            #final permutation
            for l in FP :
                Rnext.append(temp3[l-1])
            L=R[:] # Ln+1 = Rn
            R=Rnext


DEScode(" 11", 0)
