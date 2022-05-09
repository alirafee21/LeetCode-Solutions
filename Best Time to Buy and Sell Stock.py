class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        temp = 0
        if len(prices) <= 1:
            return 0
        for i in range(len(prices) - 1):
            save = prices[i+1:]
            if (save - prices[i]) > temp:
                temp = save - prices[i]
        return temp
        