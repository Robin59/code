from code import *
from random import *
import tools, unittest

def createRandomString() :
    """
Create a random string
    """
    string=''
    for i in range(randint(0,300)) :
        string+=(chr(randint(0,255)))
    return string

class TestCesar(unittest.TestCase):

    def testBase(self):
        self.assertEquals(cesarCode('a1234',1), 'b2345');
        self.assertEquals(cesarDecode('b2345',1), 'a1234');

    def testWithRandomValue(self):
        string=createRandomString()
        key=randint(0,255)
        code=cesarCode(string,key)
        self.assertEquals(cesarDecode(code,key),string)

class TestVigenere(unittest.TestCase):
    
    def testBase(self):
        self.assertEquals(vigCode('a1234',[1,2]), 'b3355');
        self.assertEquals(vigDecode('b3355',[1,2]), 'a1234');

    def testWithRandomValue(self):
        string=createRandomString()
        key= tools.vigKey(randint(1,10))
        code=vigCode(string,key)
        self.assertEquals(vigDecode(code,key),string)


class TestEnigma(unittest.TestCase):
    
    def testBase(self):
        string='abc'
        key=[[],[]]
        for x in range(0,256):
            key[0].append((x+2)%256)
            key[1].append((x+4)%256)
        self.assertEquals(enigmaCode(string,key),'gik')

    def testWithRandomValue(self):
        string=createRandomString()
        key= tools.enigmaKey(randint(0,5))
        code=enigmaCode(string,key)
        self.assertEquals(enigmaDecode(code,key),string)


class TestDESkey(unittest.TestCase):
    


    def testBase(self):
        key= [1 for i in range (64)]
        testKey=[]
        secKey=DESkeys(key)
        for i in range(16):
            testKey.append([])
            [testKey[i].append(1) for j in range (48)]
        self.assertEquals(secKey,testKey)

    def test2(self):
        key= [0 for i in range (64)]
        key[0]=1
        secKey=DESkeys(key)
        self.assertTrue(secKey[0][19]==1)
        self.assertTrue(secKey[0][randint(0,18)]==0)
        self.assertTrue(secKey[0][randint(20,47)]==0)
        #
        self.assertTrue(secKey[1][9]==1)
        self.assertTrue(secKey[2][15]==1)
        for x in range(16,48) :
            self.assertTrue(secKey[2][x]==0 )


if __name__ == '__main__' :
    unittest.main()
