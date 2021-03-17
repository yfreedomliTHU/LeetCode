# https://leetcode.com/problems/next-permutation/

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)-1
        i = n-1
        while i>=0 and nums[i]>=nums[i+1]:
            i -= 1

        if i >= 0:
            j = n
            while j>=0 and nums[i]>=nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        left, right = i+1, n
        while left<right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
