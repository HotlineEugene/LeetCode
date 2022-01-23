class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        for d in range(1, 10):
            num = d
            while num <= high and d < 10:
                if num >= low:
                    res.append(num)

                d += 1
                num = num * 10 + d
        return sorted(res)
