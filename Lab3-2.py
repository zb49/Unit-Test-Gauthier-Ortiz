import math
import unittest
#unit test función math.cell

class TestUno(unittest.TestCase):
    def testfunCeil(self):
        self.assertEqual(2, math.ceil(1.01))
        self.assertEqual(1, math.ceil(0.5))
        self.assertEqual(0, math.ceil(-0.0000000000000005))
        self.assertEqual(-1, math.ceil(-1.01))
        
if __name__ == '__main__':
    unittest.main()


