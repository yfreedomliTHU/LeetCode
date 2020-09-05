#https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # three pointer
        p1 = 0
        p2 = len(nums)-1
        tmp = p1
        while(tmp<=p2):
            if nums[tmp]==0:
                nums[p1], nums[tmp] = nums[tmp], nums[p1]
                p1 += 1
                tmp += 1
            elif nums[tmp]==2:
                nums[p2], nums[tmp] = nums[tmp], nums[p2]
                p2 -= 1
            else:
                tmp += 1
                
