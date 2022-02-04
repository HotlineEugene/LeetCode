class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {0: -1}
        s = res = 0
        for i, x in enumerate(nums):
            s = s + 1 if x else s - 1

            if s not in d:
                d[s] = i
            else:
                if i - d[s] > res:
                    res = i - d[s]
        return res
