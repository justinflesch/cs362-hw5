import unittest
import full_name

class TestCaseCube(unittest.TestCase):
    def test_average(self):
        self.assertEqual(full_name.combine_names("Rick", "Sanchez"), "Rick Sanchez")
        self.assertEqual(full_name.combine_names("Snow", "Ball"), "Snow Ball")
    def test_invalid(self):
        self.assertIsNone(full_name.combine_names(0, 1))
        self.assertIsNone(full_name.combine_names(10.0, 15.0))

if __name__ == "__main__":
    unittest.main()
