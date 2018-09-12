from collections import Counter

def possible_palindrome(s):
    c = Counter(s)
    not_even_values = [value for value in c.values() if value % 2]

    return len(not_even_values) <= 1

def is_palindrome(s):

    return s[::-1] == s