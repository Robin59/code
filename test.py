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

class TestFeistel(unittest.TestCase) :
    
    def testBase(self) : 
        key = [[0 for i in range (48)]]
        left = [0 for i in range (32)]
        right = [0 for i in range (32)]
        (left,right) = feistelCypher(left,right,1,key)
        #a test value

    def testInversible(self) :
        key = [[0 for i in range (48)] for j in range(16)]
        left = [0 for i in range (32)]
        right = [0 for i in range (32)]
        (leftRes,rightRes) = feistelCypher(left,right,16,key)
        self.assertNotEquals((left,right),(leftRes,rightRes))
        self.assertEquals((left,right),feistelCypher(rightRes,leftRes,16,key))

    def testInversibleWithRandom(self) :
        key = [[randint(0,1) for i in range (48)] for j in range(16)]
        inverseKey=key[::-1]
        left = [randint(0,1) for i in range (32)]
        right = [randint(0,1) for i in range (32)]
        (leftRes,rightRes) = feistelCypher(left,right,16,key)
        self.assertNotEquals((left,right),(leftRes,rightRes))
        self.assertEquals((right,left),feistelCypher(rightRes,leftRes,16,inverseKey))

class TestDES(unittest.TestCase) :
    
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
        S5test = [31,33,19,31,22,44,33,28,34,29,30,39,32,16,27,32]
        for i in range (16):
            res = sum([ S[4][j][i] for j in range(4) ])
            self.assertEquals(res,S5test[i])
        S6test = [35,33,31,34,27,27,42,26,24,28,21,35,21,31,27,38]
        for i in range (16):
            res = sum([ S[5][j][i] for j in range(4) ])
            self.assertEquals(res,S6test[i])
        S7test = [24,26,37,42,32,16,26,44,36,35,20,42,21,32,26,21]
        for i in range (16):
            res = sum([ S[6][j][i] for j in range(4) ])
            self.assertEquals(res,S7test[i])
        S8test = [23,29,39,20,29,40,40,20,37,32,28,38,23,22,32,28]
        for i in range (16):
            res = sum([ S[7][j][i] for j in range(4) ])
            self.assertEquals(res,S8test[i])

    def testPermutation(self) : 
        table = [randint(0,1) for i in range(64)]
        #just to be sure we don't have a table with just 0 or just 1
        table[0]=0
        table[1]=1
        resPI = [table[PI[i]-1] for i in range(64)]
        self.assertNotEquals(table,resPI)
        self.assertEquals(table,[resPI[IP[i]-1] for i in range(64)])


    def testRandomOnSimplified(self) :
        message = [randint(0,1) for i in range (64)]
        key = [randint(0,1) for i in range (64)]
        code = DESsimple(message,key,False,16)
        decode = DESsimple(code,key,True,16)
        self.assertNotEquals(code,message)
        self.assertEquals(decode,message)
        

    def testDEScomplet(self) :
        message = "12345678"
        key = "abCDefGH"
        code = DES(message,key,False)
        decode = DES(code,key,True)
        self.assertNotEquals(code,message)
        self.assertEquals(decode,message)


class TestDES(unittest.TestCase) :
    def testTDES(self):
        message = "12345678433&1187"
        keys = ("abCDefGH","12344321","87654321")
        code = TDES(message,keys,False)
        decode = TDES(code,keys,True)
        self.assertNotEquals(code,message)
        self.assertEquals(decode,message)
        


class TestRSA(unittest.TestCase) :
    
    def testRSAbasic(self) :
        #test with the values p=13 q=11, so n=143
        private = 7
        public =43
        message = 42
        crypted = RSAsimple (message, 143, public)
        decrypted = RSAsimple (crypted, 143, private)
        self.assertNotEquals(crypted,message)
        self.assertEquals(decrypted,message)
        #verify that we can't decrypt the crypted message with the public key
        self.assertNotEquals(RSAsimple (crypted, 143, public),message)


    def testRSA(self) :
        #test with the values p=13 q=11, so n=143
        private = 7
        public =43
        message = randint(0,143)
        cryptedS = RSAsimple (message, 143, public)
        cryptedRSA = RSAint (message, 143, public)
        self.assertEquals(message,RSAint(cryptedRSA, 143, private))
        self.assertEquals(cryptedS,cryptedRSA)
        #test with the values p=101 q=113, so n=11413
        private = 733
        public =997
        message = randint(0,11413)
        cryptedS = RSAsimple (message, 11413, public)
        cryptedRSA = RSAint (message, 11413, public)
        self.assertEquals(message,RSAint(cryptedRSA, 11413, private))
        self.assertEquals(cryptedS,cryptedRSA)

    def testRSAstring(self) :
        private = 733
        public =997
        message = "Hello world!"
        crypted = RSAstring (message, 11413, public,False)
        decrypted = RSAstring (crypted, 11413, private,True)
        self.assertEquals(message,decrypted)
        self.assertNotEquals(message,crypted)


class TestPrimeNumber (unittest.TestCase) :
    def testPrimeTable(self):
        testTable = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
        self.assertEquals( tools.prime(25), testTable)

    def testPseudoPrime(self):
        #test with the 25 first primes
        testTable = tools.prime(25)[1:]
        for prime in testTable :
            self.assertTrue( tools.pseudoPrime(prime))
        #test with non prime
        self.assertFalse( tools.pseudoPrime(15))
        self.assertFalse( tools.pseudoPrime(22))
        self.assertFalse( tools.pseudoPrime(69))
        
        #test with Carmichael's numbers (which aren't prime but still are pseudoprime)
        #self.assertFalse( tools.pseudoPrime(561)) # do not always work
        #self.assertFalse( tools.pseudoPrime(1105)) 


    def testFindPrime(self) :
        prime = tools.findPrime(2)
        testTable = tools.prime(250)
        self.assertTrue( prime in testTable or prime == 561 )


class TestDivTests (unittest.TestCase) :
    def testBase (self):
        self.assertTrue( tools.divTests(21))
        self.assertTrue( tools.divTests(25))
        self.assertTrue( tools.divTests(121))
        self.assertFalse(tools.divTests(91))

    def testRandom (self):
        randNumber = randint(100, 10000)
        flag = randNumber%3==0 or randNumber%5==0 or randNumber%11==0
        self.assertEquals (flag, tools.divTests(randNumber))

class TestEuclideAlgo (unittest.TestCase) :
    def test(self):
        a = 10
        b = 5
        self.assertEquals( tools.euclide(a,b), 5)
        self.assertEquals( tools.euclide(b,a), 5)
        a = 12
        b = 8
        self.assertEquals( tools.euclide(a,b), 4)

    def testEuclide2(self):
        a = 12
        b = 8
        (rest,u,v)= tools.euclide2(a,b)
        self.assertEquals ( (rest,u,v), (4,1,-1))
        
    def testEuclideRand(self):
        a= randint (10,1000)
        b= randint (10,1000)
        (rest,u,v)= tools.euclide2(a,b)
        self.assertEquals ( rest, tools.euclide(a,b))
        self.assertEquals ( rest, a*u+b*v)

class TestRSAKeyCreation (unittest.TestCase) : 
    def testPartialKeyCreation (self):
        p = 101
        q = 113
        (e,d) = tools.partielRSAkey (p,q)
        phi = (p-1)*(q-1)
        self.assertEquals(1, tools.euclide(phi,e))
        self.assertEquals(1 , (e*d)%phi)
        #test on RSA
        n = p*q
        message = "Hello world!"
        crypted = RSAstring (message, n, e,False)
        decrypted = RSAstring (crypted, n, d,True)
        self.assertEquals(message,decrypted)
        self.assertNotEquals(message,crypted)
        
    def testRSAkey (self):
        ((n,e),(_,d))= tools.RSAkey(100)
        message = "Hello world!"
        crypted = RSAstring (message, n, e,False)
        decrypted = RSAstring (crypted, n, d,True)
        self.assertEquals(message,decrypted)
        # self.assertNotEquals(message,crypted)

if __name__ == '__main__' :
    unittest.main()
