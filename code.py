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
            Lnext=[]#this is Ln+1 = Rn
            Rnext=[]#this is Rn+1 the result of the permutation and transformation
        #Lnext=R #copie?
        #expension fonction E on the left part L
        temp=[]
        for l in E :
            temp.append(L[l-1])
        print temp

DEScode(" 11", 0)
