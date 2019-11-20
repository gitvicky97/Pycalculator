import unittest

from csvreader import csvreader
from Calculator import Mycalculator


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.Calculator = Mycalculator()

    def test_instantiate_Calculator(self):
        self.assertIsInstance(self.Calculator, Mycalculator)

    def test_addition(self):
        test_data = csvreader('src/csv/TestAddition.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.Calculator.addition(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.Calculator.result, int(row['Result']))

    def test_subtraction(self):
        test_data = csvreader('src/csv/TestSubtraction.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.Calculator.subtraction(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.Calculator.result, int(row['Result']))

    def test_multiplication(self):
        test_data = csvreader('src/csv/TestMultiplication.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.Calculator.multiply(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.Calculator.result, int(row['Result']))

    
    def test_division(self):
        test_data = csvreader('src/csv/TestDivision.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertAlmostEqual(self.Calculator.division(row['Value 1'], row['Value 2']), result)
            self.assertAlmostEqual(self.Calculator.result, float(row['Result']))

    
    def test_square(self):
        test_data = csvreader('src/csv/TestSquare.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.Calculator.square_(row['Value 1']), result)
            self.assertEqual(self.Calculator.result, int(row['Result']))

    
    def test_square_root(self):
        test_data = csvreader('src/csv/TestSquareRoot.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertAlmostEqual(self.Calculator.sqrt_(row['Value 1']), result)
            self.assertAlmostEqual(self.Calculator.result, float(row['Result']))


if __name__ == '__main__':
    unittest.main()
