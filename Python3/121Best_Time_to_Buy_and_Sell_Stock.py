#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        MIN = prices[0]
        ans = 0
        for i in range(n):
            cur_pro = prices[i] - MIN
            if cur_pro <= 0:
                MIN = prices[i]
            else:
                ans = max(ans, cur_pro)
                
        return ans
