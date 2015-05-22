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



print enigmaKey(2)
