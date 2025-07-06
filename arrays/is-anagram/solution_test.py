import unittest
from solution import isAnagram

class TestIsAnagram(unittest.TestCase):
    def test_example1(self):
        self.assertTrue(isAnagram(None, "anagram", "nagaram"))
    def test_example2(self):
        self.assertFalse(isAnagram(None, "rat", "car"))
    def test_empty(self):
        self.assertTrue(isAnagram(None, "", ""))
    def test_case_sensitive(self):
        self.assertFalse(isAnagram(None, "a", "A"))
    def test_diff_length(self):
        self.assertFalse(isAnagram(None, "abc", "ab"))

if __name__ == "__main__":
    unittest.main()
