class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        multiplier = 1
        score = 0
        closing = False
        for elem in s:
            if elem == "(":
                multiplier <<= 1
                closing = False
            else:
                multiplier >>= 1
                score += multiplier * (not closing)
                closing = True

        return score
