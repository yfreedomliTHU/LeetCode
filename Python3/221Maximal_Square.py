#https://leetcode.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        #dp dp(i,j)表示包含该点为右下角的最大正方形的变长
        #dp(i,j)=min(dp(i−1,j),dp(i−1,j−1),dp(i,j−1))+1
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        max_len = 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i==0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])+1
                    max_len = max(max_len, dp[i][j])
                    
        return max_len**2
