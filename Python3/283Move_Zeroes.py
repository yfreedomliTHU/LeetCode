#https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        count = 0
        for i in range(len(nums)):
            index = i - count
            if nums[index] == 0:
                nums.pop(index)
                nums.append(0)
                count += 1
        '''
        #double pointer
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
        
