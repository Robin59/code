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
