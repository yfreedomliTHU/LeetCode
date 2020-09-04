#https://leetcode.com/problems/minimum-path-sum/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #dp[i][j]=min(dp[i−1][j],dp[i][j−1])+grid[i][j]
        #注意边界情况
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if i==j==0: continue
                elif i==0 and j > 0:
                    grid[i][j] += grid[i][j-1]
                elif i>0 and j ==0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[-1][-1]
