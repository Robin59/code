#!/usr/bin/env python




def cesarCode(string,key):
    res = ''
    for char in string :
    	res+=chr(ord(char)+key)
    return res

def cesarDecode(string,key):
    res = ''
    for char in string :
    	res+=chr(ord(char)-key)
    return res

#test
codeValue = cesarCode('a1234',1)
baseValue = cesarDecode(codeValue,1)
print 'cesar code with value=a1234 and key=1'
print 'code :'
print codeValue
print 'decode :'
print baseValue
