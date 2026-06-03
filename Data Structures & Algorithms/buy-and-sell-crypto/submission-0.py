class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        ptr1 = 0
        ptr2 = n - 1

        max_profit = 0

        for i in range(n):
            curr_profit = 0
            if prices[0:i]:
                curr_profit = prices[i] - min(prices[0:i])
            else:
                continue

            if curr_profit > max_profit:
                max_profit = curr_profit
        
        return max_profit