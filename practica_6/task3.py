import unittest
import lib

import math
math.pi

class LibTest(unittest.TestCase):

     def test_sin(self):
        self.assertEqual(lib.sin(0), 0)
        self.assertEqual(lib.sin(math.pi), 0)
        self.assertEqual(lib.sin((math.pi)/2), 1)
        self.assertEqual(lib.sin(-(math.pi)/2), -1)

unittest.main(verbosity=2)
