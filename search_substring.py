"""
Поиск подстроки в строке
"""

from string_equality_check import string_equality_check


def search_substring(s, sub):
    for i in range(0, len(s) - len(sub)):
        if string_equality_check(s[i:i+len(sub)], sub):
            print(i)


s = "abcasbacajcbajcbajcbajbcajbcjabcjabcjabcjabcjabcacabcabc"
sub = "abc"
print(search_substring(s, sub))
