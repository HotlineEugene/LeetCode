# Given two strings a and b, return the minimum number of times you should repeat string a so that string b is a
# substring of it. If it is impossible for b
# to be a substring of a after repeating it, return -1.


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:

        s_fold = "".join((s[1:], s[:-1]))

        return s in s_fold
