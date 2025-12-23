import unittest
from domain.calculations import Calculations

class TestCalculation(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.calculation = Calculations(8, 2)

    def test_sum(self):
        self.assertEqual(self.calculation.get_sum(), 10)

    def test_diff(self):
        self.assertEqual(self.calculation.get_difference(), 6)


if __name__ == '__main__':
    unittest.main()