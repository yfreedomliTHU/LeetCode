#https://leetcode.com/problems/perfect-squares/


class Solution:
    def numSquares(self, n: int) -> int:
       
        '''
        #1.DP:numSquares(n)=min(numSquares(n-k) + 1) 
        square_nums = [i**2 for i in range(0, int(math.sqrt(n))+1)]
        
        dp = [float('inf')] * (n+1)
        # bottom case
        dp[0] = 0
        
        for i in range(1, n+1):
            for square in square_nums:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i-square] + 1)
        
        return dp[-1]
        '''
        #2贪心枚举
        square_nums = [i**2 for i in range(0, int(math.sqrt(n))+1)]
        def divided(n, count):
            if count == 1:
                return n in square_nums
            for k in square_nums:
                if divided(n-k, count-1):
                    return True
            return False
        
        for count in range(1, n+1):
            if divided(n, count):
                return count
