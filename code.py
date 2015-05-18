#!/usr/bin/env python



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


#Inspired by Enigma but simplified
def eniCode(message,key) :
    """
    """
    res=''
    length=len(key)
    i=0
    for char in string :
        res+=chr((key[(i+ord(char))%length])%256)
        i+=1
    return res

def eniDecode(message,key) :
    res=''
    length=len(key)
    i=0
    for char in string :
        res+=chr((key[(i-ord(char))%length])%256)
        i+=1
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
print 'Enigma code with value=a1234 and key='
#codeValue = vigCode('a1234',)
#baseValue = vigDecode(codeValue,)
print 'code :'
#print codeValue
print 'decode :'
print baseValue

