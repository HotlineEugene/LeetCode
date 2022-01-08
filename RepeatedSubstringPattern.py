# Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if not str:
            return False

        ss = (s + s)[1:-1]
        return ss.find(s) != -1
