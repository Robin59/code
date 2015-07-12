#tools use for the cryptographie
from random import *


#Create a key for the enigma cypher
def enigmaKey (nbRings) :
    """
    Create a key for the enigma cypher, 
    nbRings is the number of rings contain in the key
    """
    key=[]
    for a in range(nbRings) :
        list = range(256)
        subKey = []
        for i in range (256) :
            subKey.append(list.pop(randint(0,255-i)))
        key.append(subKey)
    return key


#Create a key for the Vigenere cypher
def vigKey (length) :
    """
    Create a key for the Vigenere cypher, 
    length is the length of the key
    """
    key=[]
    for i in range(length):
        key.append(randint(0,255))
    return key


# create a table with prime nombers

def prime(length) :
    """
Length is the lenght of the table which means that how many prime numbers it will contain. The primes are always clacified by ascending order
    """
    tab = [2,3]
    current = 5
    while (len(tab)<length) :
        i=0
        while (current%tab[i] !=0 and current>=tab[i]**2) :
            i+=1
        #we check if the reason why we leave the while condition is because the current number is prime
        if ( current%tab[i] != 0 ) :
            #if it's a prime number we add it to the table
            tab.append(current)
        #now we can check for the next odd nomber
        current+=2
    #
    return tab


# Test if a number is prime

def pseudoPrime(n) :
    """
Test if a number n  is pseude prime, which mean it's probaly prime, but don't always work specialy never work with Carmichael's numbers that arn't prime but are pseudo prime
    """
    result = True
    i = 1
    while(result and i<5 ) :
        b = randint(2,n)
        if( (b**(n-1))%n != 1 and b!=n ) :
            result = False
        i+=1
    return result
        

def findPrime (n) :
    """
Try to find a random prime number between the numbers n and n+1000.
    """
    n = n + randint(1,1000)
    if (n%2 == 0) : 
        n+=1
    while ( not pseudoPrime(n) ) :
        n+=2
    return n

# Euclide algorithm (to calculat biggest multiple between two numbers)

def euclide(a, b) :
    """
find the biggest multiple between two numbers (a and b)
    """
    #check that a>b 
    if (b>a) : 
        a, b = b , a
    while (True) :
        a, b = b, a%b
        if (b == 0) :
            break
    return a
        
def euclide2(a,b) :
    """
find the greatest multiple between two numbers (a and b) and give u and v with r=a*u+b*v)
    """
    r, u, v, r2, u2, v2 = a,1,0,b,0,1
    #check that a>b 
    if (b>a) :  
        r, r2 = r2, r
    while ( r2 != 0) :
        q = r/r2
        r, u, v, r2, u2, v2 = r2,u2,v2,r-q*r2,u-q*u2,v-q*v2
    if (b>a) :
        return (r,v,u)
    return (r,u,v)
        
