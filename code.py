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

#Initial permutation
PI= [58,50,40,42,34,26,18,10,2,60,52,44,36,28,20,12,4,62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8,57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7]
#inverse of the inital permutation
IP= [40,8,48,16,56,24,64,32,39,7,47,15,55,23,63,31,38,6,46,14,54,22,62,30,37,5,45,13,53,21,61,29,36,4,44,12,52,20,60,28,35,3,43,11,51,19,59,27,34,2,42,10,50,18,58,26,33,1,41,9,49,17,57,25]

E=[32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,12,13,12,13,14,15,16,17,16,17,18,19,20,21,20,21,22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1]

#The 8 S tables are put in one, the first index is for the number of the table 
S=[[[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],[0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],[4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],[15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]] , [[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],[3,13,4,7,15,2,8,14,13,0,1,10,6,9,11,5],[0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],[13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]] , [[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],[13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],[13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],[1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]] , [[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],[13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],[10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],[3,15,0,6,10,1,3,8,9,4,5,11,12,7,2,14]] , [[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],[14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],[4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],[11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]] , [[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],[10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],[9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],[4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]],[[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],[13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],[1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],[6,11,13,8,1,4,10,7,9,0,5,15,14,2,3,12]] , [[13,2,8,4,6,15,11,11,10,9,3,14,5,0,12,7],[1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],[7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],[3,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]]

#table for the last permutation 
FP=[16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25]

def DEScode(string,key) : 
    lengthString = len(string)
    res=''
    #check if the key is from a correct longer and transform it in a table of byte 
    lengthKey = len(key)
    while (lengthKey%8 != 0) :
        key+=(" ")
        lengthKey+=1
    keyB=[]
    for char in key : 
        for byte in ('{0:08b}'.format(ord(char))) : 
            keyB.append(int(byte))
    #contruction of the secondary keys
    keys = DESkeys(keyB)
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
        for j in range(32) :  #IT'S NOT LEFT AND RIGHT BUT UPPER AND DOWN
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
            temp2=[(int(temp[x])+keys[j][x])%2 for x in range (48)]
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
        #now that 8 characters have been cypher we apply the inverse of the initial permutation
        finalTab=[]# VERIFY IF IT'S LEFT AND RIGHT OR UPPER AND DOWN
        for j in range(32) :
            finalTab.append(int(L[j]))
        for j in range(32) :
            finalTab.append(int(R[j]))
        #we convert the byte in char
        for j in range(8) :
            res+=chr((finalTab[j*8]+finalTab[j*8+1]*2+finalTab[j*8+2]*4+finalTab[j*8+3]*8+finalTab[j*8+4]*16+finalTab[j*8+5]*32+finalTab[j*8+6]*64+finalTab[j*8+7]*128)%256)
    return res

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

