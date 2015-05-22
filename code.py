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



#test

print 'cesar code with value=a1234 and key=1'
codeValue = cesarCode('a1234',228)
baseValue = cesarDecode(codeValue,228)
print 'code :'
print codeValue
print 'decode :'
print baseValue
print 'Vigenere code with value=a1234 and key=[1,2]'
codeValue = vigCode('a1234',[228,2])
baseValue = vigDecode(codeValue,[228,2])
print 'code :'
print codeValue
print 'decode :'
print baseValue
#enigma test
eKey=tools.enigmaKey(4)
print 'Enigma code with value=a1234'
print eKey
codeValue = enigmaCode('a1234',eKey)
baseValue = enigmaDecode(codeValue,eKey)
print 'code :'
print codeValue
print 'decode :'
print baseValue

