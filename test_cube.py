import unittest
import cube

class TestCaseCube(unittest.TestCase):
    def test_cube(self):
        self.assertEqual(cube.cube_it(5, 5, 5), 125)
        self.assertEqual(cube.cube_it(10, 10, 10), 1000)
        self.assertEqual(cube.cube_it(2, 10, 10), 200)
    def test_neg_values(self):
        self.assertIsNone(cube.cube_it(-10, 10, 10))
        self.assertIsNone(cube.cube_it(10, -10, 10))
        self.assertIsNone(cube.cube_it(10, 10, -10))
        self.assertIsNone(cube.cube_it(0, 10, 10))
        self.assertIsNone(cube.cube_it(10, 0, 10))
        self.assertIsNone(cube.cube_it(10, 10, 0))
    def test_invalid(self):
        self.assertIsNone(cube.cube_it("a", 10, 10))
        self.assertIsNone(cube.cube_it(10, "b", 10))
        self.assertIsNone(cube.cube_it(10, 10, "c"))

if __name__ == "__main__":
    unittest.main()
