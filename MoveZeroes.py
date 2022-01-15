class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0
        for i in range(len(nums)):
            if nums[i - j] == 0:
                del nums[i - j]
                j += 1

        for _ in range(j):
            nums.append(0)
