#https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        #贪心 + dp
        #dp[i] = max(dp[i-2] + nums[i], dp[i-1]) 
        #边界：dp[0] = nums[0], dp[1] = max(nums[0], nums[1])
        if not nums:
            return 0
        if len(nums) < 2:
            return nums[0]
        n = len(nums)
        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
            
        return dp[-1]
