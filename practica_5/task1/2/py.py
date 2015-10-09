import unittest
import lib

class LibTest(unittest.TestCase):

    def even(self):
        self.assertEqual(lib.even(2), 'chetnoe')
        self.assertEqual(lib.sqrt(1), 'nechetnoe')
        self.assertEqual(lib.sqrt(0), '')

    def factoria(self):
        self.assertEqual(lib.factorial(0), 1)
        self.assertEqual(lib.factorial(3), 6)
        self.assertEqual(lib.factorial(-1), 0)

    def palindrome(self):
        self.assertEqual(lib.palidrome(121), 'palidrome')
        self.assertEqual(lib.palidrome(304), 'non palidrome')
        self.assertEqual(lib.palidrome(-1), 'palidrome')

    def prime(self):
        self.assertEqual(lib.prime(7), 'prostoe')
        self.assertEqual(lib.prime(6), 'ne prostoe')
        self.assertEqual(lib.prime(0), 'ne prostoe')
        self.assertEqual(lib.prime(-1), 'ne prostoe')

    def sin(self):
        self.assertEqual(lib.sin(0), 0)
        self.assertEqual(lib.sin(Pi), '0')
        self.assertEqual(lib.sin(Pi/2), '1')
        self.assertEqual(lib.sin(-Pi/2), '-1')










unittest.main(verbosity=2)