class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i-j] == 0:
                del nums[i-j]
                j += 1
                
        for _ in range(j):
            nums.append(0)
