class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        firstNum, secondNum, targetNum = "", "", ""

        for s in firstWord:
            firstNum += str(ord(s) - ord("a"))

        for s in secondWord:
            secondNum += str(ord(s) - ord("a"))

        for s in targetWord:
            targetNum += str(ord(s) - ord("a"))

        return int(firstNum) + int(secondNum) == int(targetNum)
