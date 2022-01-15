class Solution:
    def isUgly(self, n: int) -> bool:
        def divide_all(divisor):
            nonlocal n
            while n > 1 and n % divisor == 0:
                n //= divisor

        if n < 1:
            return False

        divide_all(2)
        divide_all(3)
        divide_all(5)

        return n == 1
