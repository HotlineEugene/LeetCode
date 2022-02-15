class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        L = len(nums)
        dp = [0 for _ in range(L)]
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, L):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1]
