class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        for i in range(len(prices)):
            currProfit = 0

            if prices[0:i]:
                currProfit = prices[i] - min(prices[0:i])
            else:
                continue

            if currProfit > maxProfit: maxProfit = currProfit
        
        return maxProfit