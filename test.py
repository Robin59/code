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




if __name__ == '__main__' :
    unittest.main()
