#https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        #dp[i][j] = dp[i][j-1]+dp[i-1][j]
        dp = [[0]*m for _ in range(n)]
        for i in range(n):
            dp[i][0] = 1
        for j in range(m):
            dp[0][j] = 1
        
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i][j-1]+dp[i-1][j]
        
        return dp[-1][-1]
        '''
        # reduce space consume
        #dp[i] = dp[i-1]+dp[i]
        dp = [1]*m
        for i in range(1, n):
            for j in range(1, m):
                dp[j] = dp[j-1]+dp[j]
        return dp[-1]
