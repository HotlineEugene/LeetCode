class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = -999999999
        cursum = 0
        for i in range(0, len(nums)):
            cursum += nums[i]
            if cursum > maxsum:
                maxsum = cursum
            if cursum < 0:
                cursum = 0
        return maxsum
