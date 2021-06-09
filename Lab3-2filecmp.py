import filecmp
import unittest

# Unit test funcion filecomp

file1 = "C:\\Users\ortizga\Documents\practicaPy\HolaMundo.txt"
file2 = "C:\\Users\ortizga\Documents\practicaPy\HolaMundoII.txt"

class TestDos(unittest.TestCase):
        def testfunfilecmp(self):
            self.assertTrue(filecmp.cmp(file1, file2, shallow=False))

if __name__ == '__main__':
    unittest.main()
