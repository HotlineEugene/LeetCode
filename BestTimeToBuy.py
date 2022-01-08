# Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not len(prices):
            return 0
        buy = prices[0]
        profit = 0
        for p in prices[1:]:
            if p - buy > profit:
                profit = p - buy
            elif p < buy:
                buy = p
        return profit
