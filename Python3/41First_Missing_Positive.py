#https://leetcode.com/problems/first-missing-positive/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        '''
        # 1.hash
        n = len(nums)
        
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
        
        for i in range(n):
            tmp = abs(nums[i])
            if tmp <= n:
                nums[tmp-1] = -abs(nums[tmp-1])
                
        for i in range(n):
            if nums[i] > 0:
                return i+1
        
        return n+1
        '''
        # 2swap
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i]- 1]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
