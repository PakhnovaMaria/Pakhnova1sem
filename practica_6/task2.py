import unittest
import lib

import math

class LibTest(unittest.TestCase):

    def test_even_even(self):

        self.assertEqual(lib.even(2), True)

    def test_even_odd(self):
        self.assertEqual(lib.even(1), False)

    def test_factorial(self):
        self.assertEqual(lib.factorial(0), 1)
        self.assertEqual(lib.factorial(3), 6)
        self.assertEqual(lib.factorial(-1), 0)

    def test_palindrome(self):
        self.assertEqual(lib.palidrome(121), True)
        self.assertEqual(lib.palidrome(304), False)
        self.assertEqual(lib.palidrome(-1), True)

    def test_prime_prime(self):
        self.assertEqual(lib.prime(5), True)

    def test_prime_notprime(self):
        self.assertEqual(lib.prime(4), False)
        self.assertEqual(lib.prime(-1), False)


    def test_sin(self):
        self.assertEqual(lib.sin(0), 0)
        self.assertEqual(lib.sin(math.pi), 0)
        self.assertEqual(lib.sin((math.pi)/2), 1)
        self.assertEqual(lib.sin(-(math.pi)/2), -1)

if __name__ == '__main__':
    unittest.main(verbosity = 2)








