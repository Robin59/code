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


class testDES(unittest.TestCase) :
    
    def testTable(self) :
        #PI table's test
        PItest=[240,256,272,288,232,248,264,280]
        for i in range (8):
            res = sum([ PI[i*8+j] for j in range (8)])
            self.assertEquals(res,PItest[i])
        #PI table's test
        IPtest=[288,280,272,264,256,248,240,232]
        for i in range (8):
            res = sum([ IP[i*8+j] for j in range (8)])
            self.assertEquals(res,IPtest[i])
        #table E (extension's fonction)
        Etest = [80,52,56,60,64,68,64,68,72,76,80,52]
        for i in range(12):
            res = sum([ E[j*12+i] for j in range (4)])
            self.assertEquals(res, Etest[i])
        #FP table
        FPtest=[38,43,97,67,88,68,66,61]
        for i in range(8):
            res = sum([ FP[j*8+i] for j in range(4) ])
            self.assertEquals(res,FPtest[i])
        #S1 table
        S1test = [33,32,42,15,33,32,27,27,33,39,30,44,27,24,14,28]
        for i in range (16) : 
            res = sum([ S[0][j][i] for j in range(4) ])
            self.assertEquals(res,S1test[i])
        S2test = [31,36,29,33,34,32,28,21,37,21,22,41,27,17,32,39]
        for i in range (16):
            res = sum([ S[1][j][i] for j in range(4) ])
            self.assertEquals(res,S2test[i])
        #S3
        S3test = [37,23,26,32,23,31,32,22,18,37,33,36,39,30,33,28]
        for i in range (16):
            res = sum([ S[2][j][i] for j in range(4) ])
            self.assertEquals(res,S3test[i])
        #S4
        S4test =[33,42,34,14,28,33,29,34,29,14,18,42,29,31,28,42]
        for i in range (16):
            res = sum([ S[3][j][i] for j in range(4) ])
            self.assertEquals(res,S4test[i])

    def testBase(self) :
        message ="12345678"
        key = '\x00\x00\x00\x00\x00\x00\x00\x00'
        #code = DEScode(message,key,False)
        #self.assertEquals(code,message)
        key = "12345678"
        #self.assertNotEquals(code,message)
        #self.assertEquals(DEScode(code,key,True),message)

if __name__ == '__main__' :
    unittest.main()
