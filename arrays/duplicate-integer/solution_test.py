import unittest
from solution import containsDuplicate

class TestContainsDuplicate(unittest.TestCase):
    def test_example1(self):
        self.assertTrue(containsDuplicate(None, [1, 2, 3, 1]))
    def test_example2(self):
        self.assertFalse(containsDuplicate(None, [1, 2, 3, 4]))
    def test_example3(self):
        self.assertTrue(containsDuplicate(None, [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
    def test_empty(self):
        self.assertFalse(containsDuplicate(None, []))
    def test_single(self):
        self.assertFalse(containsDuplicate(None, [1]))

if __name__ == "__main__":
    unittest.main()
