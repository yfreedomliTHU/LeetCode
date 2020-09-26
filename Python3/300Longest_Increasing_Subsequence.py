#https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        #1.DP O(n^2)
        #dp[i] = max(dp[i], dp[j] + 1) for j in [0, i)
        if not nums:
            return 0
        n = len(nums)
        dp = [1]*n
        dp[0] = 1
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
        '''
        #dp + binary
        if not nums:
            return 0
        n = len(nums)
        tails = [0]*n
        ans = 0
        for num in nums:
            l, r = 0, ans
            while l < r:
                mid = l + (r-l)//2
                if tails[mid] < num:
                    l = mid + 1
                else:
                    r = mid
            tails[l] = num
            if r == ans:
                ans += 1
        return ans
