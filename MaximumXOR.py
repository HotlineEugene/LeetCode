class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        mask, maximum = 0, 0
        for i in range(31, -1, -1):
            mask = mask | 1 << i
            prefixPartSet = {mask & num for num in nums}

            checkingPossibilityOfObtaining = maximum | 1 << i
            for prefix in prefixPartSet:
                if checkingPossibilityOfObtaining ^ prefix in prefixPartSet:
                    maximum = checkingPossibilityOfObtaining
                    break
        return maximum
