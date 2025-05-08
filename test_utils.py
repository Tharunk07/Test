import unittest

from addition import add, sub

class Test(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5,10),15)
        self.assertEqual(add(10,10),20)
    def test_sub(self):
        self.assertEqual(sub(10,5),5)
        self.assertEqual(sub(10,20),-10)

if __name__ == '__main__':
    unittest.main()