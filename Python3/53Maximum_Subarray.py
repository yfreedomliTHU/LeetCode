# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        # 1.
        tmp = nums[0]
        Max = tmp
        n = len(nums)
        for i in range(1, n):
            if (tmp + nums[i]) > nums[i]:
                Max = max(Max, tmp+nums[i])
                tmp = tmp+nums[i]
            else:
                Max = max(Max, tmp, tmp+nums[i], nums[i])
                tmp = nums[i]   
        return Max
        '''
        '''
        #2
        maxcur = nums[0]
        maxglobal = nums[0]
        for i in range(1, len(nums)):
            maxcur = max(nums[i], maxcur+nums[i])
            maxglobal = max(maxglobal, maxcur)
        return maxglobal
        '''
        #3 分治法
        n = len(nums)
        if n == 1: return nums[0]
        else:
            max_l = self.maxSubArray(nums[:n//2])
            max_r = self.maxSubArray(nums[n//2:])
        #计算中间的最大值
        max1 = nums[n//2-1]
        tmp = 0
        for i in range(n//2-1, -1, -1):
            tmp += nums[i]
            max1 = max(max1, tmp)
        max2 = nums[n//2]
        tmp = 0
        for i in range(n //2, n):
            tmp += nums[i]
            max2 = max(max2, tmp)
            
        max_m = max1+max2
        
        return max(max_l, max_r, max_m)
