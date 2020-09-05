#https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        #f[n] = f[n-1]+f[n-2]
        if n == 1:
            return 1
        elif n == 2:
            return 2
        ans = [0]*n
        ans[0], ans[1] = 1, 2
        for i in range(2, n):
            ans[i] = ans[i-1] + ans[i-2]
            
        return ans[-1]
        
