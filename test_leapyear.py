import unittest
import leapyear

class TestFunction(unittest.TestCase):
    def test_func(self):
        # function should return 1 if leap year, 0 if not
        self.assertEqual(leapyear.leaptest(0), 0)
        self.assertEqual(leapyear.leaptest(4), 1)
        self.assertEqual(leapyear.leaptest(7), 0)
        self.assertEqual(leapyear.leaptest(8), 1)
        self.assertEqual(leapyear.leaptest(100), 0)
        self.assertEqual(leapyear.leaptest(200), 0)
        self.assertEqual(leapyear.leaptest(400), 1)
    def test_invalid_func(self):
        self.assertIsNone(leapyear.leaptest(-10))
        self.assertIsNone(leapyear.leaptest("abc"))

if __name__ == "__main__":
    unittest.main()
