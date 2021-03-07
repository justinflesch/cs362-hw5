import unittest
import fizzbuzz

class TestCaseCube(unittest.TestCase):
    def test_average(self):
        self.assertIsNotNone(fizzbuzz.fizzer(1)
        self.assertIsNotNone(fizzbuzz.fizzer(3)
        self.assertIsNotNone(fizzbuzz.fizzer(9)
        self.assertIsNotNone(fizzbuzz.fizzer(10)
        self.assertIsNotNone(fizzbuzz.fizzer(20)
        self.assertIsNotNone(fizzbuzz.fizzer(30)
        self.assertIsNotNone(fizzbuzz.fizzer(100)
        self.assertIsNotNone(fizzbuzz.fizzer(300)
    def test_invalid(self):
        self.assertIsNone(fizzbuzz.fizzer({-1))
        self.assertIsNone(fizzbuzz.fizzer({-100}))
        self.assertIsNone(fizzbuzz.fizzer({"abcdef"}))

if __name__ == "__main__":
    unittest.main()
