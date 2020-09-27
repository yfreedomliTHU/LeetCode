#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #dp
        #f[i][0]=max(f[i−1][0],f[i−1][2]−prices[i])
        #f[i][1]=f[i−1][0]+prices[i]
        #f[i][2]=max(f[i−1][1],f[i−1][2])
        #max(f[n−1][1],f[n−1][2])
        if not prices:
            return 0
        n = len(prices)
        f0, f1, f2 = -prices[0], 0, 0
        for i in range(1, n):
            f0_tmp = max(f0, f2-prices[i])
            f1_tmp = f0 + prices[i]
            f2_tmp = max(f1, f2)
            f0, f1, f2 = f0_tmp, f1_tmp, f2_tmp
        
        return max(f1, f2)
