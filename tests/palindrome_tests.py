import unittest
from functions import is_palindrome, possible_palindrome


is_pal_test_data = ['', 'pop', 'rsoi', 'd', 'tttttttttttttttttttttt', 'oiuuio', 'abcdefdcba']
is_pal_test_result = [True, True, False, True, True, True, False]

pos_pal_test_data = ['', '112233', 'bbbaa', 'opp', 'abcd', '@', 'ttar']
pos_pal_test_result = [True, True, True, True, False, True, False]


class TestPalindrome(unittest.TestCase):

    def test_is_palindrome(self):
        for i, item in enumerate(is_pal_test_data):
            with self.subTest(text="sequence: "+item):
                self.assertEqual(is_palindrome(item), is_pal_test_result[i])

    def test_possible_palindrome(self):
        for i, item in enumerate(pos_pal_test_data):
            with self.subTest(text="sequence: "+item):
                self.assertEqual(possible_palindrome(item), pos_pal_test_result[i])

if __name__ == '__main__':
    unittest.main()
        