class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #ans = []
        profit = 0
        left, right = 0, 1
        for right in range(len(prices)):
            if prices[left] > prices[right]:
                left = right
            else:
                p = prices[right] - prices[left]
                profit = max(profit, p)
    
        return profit
