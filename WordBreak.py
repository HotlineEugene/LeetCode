class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        new = set()
        for i in wordDict:
            new.add((i, len(i)))
        words = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j, k in new:
                if k <= i and s[(i - k) : i] == j and dp[i - k] == True:
                    dp[i] = True
                    break
        print(dp)
        return dp[-1]
