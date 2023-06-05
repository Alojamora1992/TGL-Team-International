import unittest
from exercise1 import is_palindrome

class PalindromeTest(unittest.TestCase):

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("radar"))
        self.assertFalse(is_palindrome("hello"))
        self.assertTrue(is_palindrome("level"))
        self.assertFalse(is_palindrome("python"))
        self.assertTrue(is_palindrome("madam"))

if __name__ == "__main__":
    unittest.main()