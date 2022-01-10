class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(1, len(digits) + 1):
            if digits[-1 * i] != 9:
                digits[-1 * i] += 1
                return digits

            else:
                digits[-1 * i] = 0

        digits.insert(0, 1)

        return digits
