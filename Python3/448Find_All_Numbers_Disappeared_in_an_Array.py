#https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        '''
        #1.
        ans = []
        n = len(nums)
        for i in range(n):
            while nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        for i, val in enumerate(nums):
            if val != i+1:
                ans.append(i+1)
        return ans
        '''
        #2.abs
        res = []
        for i in range(len(nums)):
            loc = abs(nums[i]) - 1 
            if nums[loc] > 0:
                nums[loc] = -nums[loc]
        for idx, val in enumerate(nums, 1):
            if val > 0:
                res.append(idx)
        return res
