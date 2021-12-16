import sys
import os
import unittest

import_path = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(import_path)

from function.mul import mul

class TestingMul(unittest.TestCase):
    
    def testSum_twoPositivNumbers_sumOfTwoNumbers(self):
        a = 5
        b = 3
        mul_expected = 15
        result = mul(a, b)
        self.assertEqual(result, mul_expected)
    
