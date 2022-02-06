class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = 1
        k = 0
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                val = nums[i]
                while i + 1 < len(nums) and nums[i + 1] == val:
                    k += 1
                    nums[i + 1] = nums[-1] + 1
                    i += 1
            i += 1
        nums.sort()
        return n - k
