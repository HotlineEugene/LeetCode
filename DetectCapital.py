class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word in (word.upper(), word.capitalize(), word.lower())
