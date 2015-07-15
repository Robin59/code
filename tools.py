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
    # divTests complexity is less important than pseudoPrime
    while (divTests(n) or not pseudoPrime(n) ) :
        n+=2
    return n

def divTests(n) :
    """
Use divisibility tests to check if n is mutiple of 3, 5 or 11
    """
    #not sure about the computational complexity of this line and if there is a better way to do it 
    tab = [ int(a) for a in str(n) ]
    if (tab[len(tab)-1] == 5) :
        return True
    elif(sum(tab) % 3 == 0) :
        return True
    else :
        sumAlt=0
        flag = False
        for x in tab :
            if (flag) :
                sumAlt +=x
            else :
                sumAlt -=x
            flag = not flag
        return sumAlt%11 == 0

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
        
# tools for creating keys for RSA cypher

def partielRSAkey (p,q):
    """
create e (a public key) and d (private key) from 2 prime number p and q
    """
    phi = (p-1)*(q-1)
    e = phi-2 # should had some randomness for the first e
    (rest,_,d)= euclide2(phi,e)
    # we test if phi and e are prime between them
    while (rest!=1) :
        e -= 1
        (rest,_,d)= euclide2(phi,e)
        #should raise an exception if no number found (occure with small numbers)
    return (e,d)

def RSAkey (x) :
    """
Create the keys((n,e),(n,d)) for the RSA cypher. The prime numbers are gonna be bigger than x.
    """
    #create 2 different prime numbers
    while (True) :
        p = findPrime(x)
        q = findPrime(x+1000)
        n = p*q
        (e,d) = partielRSAkey (p,q)
        if (p!=q and d>0) :
            return ((n,e),(n,d))
    
