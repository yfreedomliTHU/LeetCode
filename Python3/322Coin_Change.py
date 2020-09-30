#https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #DP
        #f[j] = min(f[j], f[j-ci] + 1) 总价值j
        #f[0] = 0
        f = [float('inf')] * (amount + 1)
        f[0] = 0
        for c in coins:
            for j in range(c, amount+1):
                f[j] = min(f[j], f[j - c] + 1)
        return f[amount] if f[amount]!=float('inf') else -1
        
        
