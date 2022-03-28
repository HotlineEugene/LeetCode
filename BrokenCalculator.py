class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        ops = 0

        while target != startValue:
            if target > startValue and target % 2 == 0:
                ops += 1
                target //= 2

            elif target > startValue:
                diff = target
                target += 1
                ops += 1

            elif target < startValue:
                ops += startValue - target
                target = startValue
        return ops
