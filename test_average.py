import unittest
import average

class TestCaseCube(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average.avg_list({5, 10, 15}), 10)
        self.assertEqual(average.avg_list({10, 10, 10}), 10)
        self.assertEqual(average.avg_list({25, 50, 75}), 50)
    def test_neg_values(self):
        self.assertEqual(average.avg_list({-10, 0, 10}), 0)
        self.assertEqual(average.avg_list({-100, -50, 0}), -50)
        self.assertEqual(average.avg_list({-100, -200, -300}), -200)
    def test_invalid(self):
        self.assertIsNone(average.avg_list({"a", 10, 10}))
        self.assertIsNone(average.avg_list({10, "b", 10}))
        self.assertIsNone(average.avg_list({10, 10, "c"}))

if __name__ == "__main__":
    unittest.main()
