class Solution:
    def countOrders(self, n: int) -> int:
        n = 2 * n
        ans = 1
        while n >= 2:
            ans = ans * ((n * (n - 1)) // 2)
            n -= 2
            ans = ans % 1000000007
        return ans
