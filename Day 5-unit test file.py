# Author: Gan Li
# Date: 9/28/21 9:18 下午
# Description:
import unittest
from a2021_09_28_module import multiply_3_numbers as mul


class Test(unittest.TestCase):
    """
    4 tests for function mul
    """
    def test_1(self):
        result = mul(1, 2, 3)
        self.assertEqual(result, 6)

    def test_2(self):
        result = mul(2, 4, 8)
        self.assertEqual(64, result)

    def test_3(self):
        result = mul(1.2, 1, 5)
        self.assertAlmostEqual(result, 6.0, 1)

    def test_4(self):
        result = mul(0, 1, 5)
        self.assertNotAlmostEqual(result, 1.1, 1)


if __name__ == '__main__':
    unittest.main()
