#https://leetcode.com/problems/number-of-islands/

class Solution:
    def dfs(self, grid, m, n):
        grid[m][n] = 0
        x_dim, y_dim = len(grid), len(grid[0])
        for x, y in [(m-1, n), (m+1,n), (m, n-1),(m,n+1)]:
            if 0<=x<x_dim and 0<=y<y_dim and grid[x][y]=='1':
                self.dfs(grid, x, y)
    def numIslands(self, grid: List[List[str]]) -> int:
        #DFS
        x_dim = len(grid)
        if x_dim == 0:
            return 0
        y_dim = len(grid[0])
        ans = 0
        for i in range(x_dim):
            for j in range(y_dim):
                if grid[i][j] == '1':
                    ans += 1
                    self.dfs(grid, i, j)
        
        return ans
