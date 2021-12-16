import sys
import os
import unittest

import_path = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(import_path)

from function.sum import sum

class TestingSum(unittest.TestCase):
    
    def testSum_twoPositivNumbers_sumOfTwoNumbers(self):
        a = 5
        b = 3
        sum_expected = 8
        result = sum(a, b)
        self.assertEqual(result, sum_expected)
    
