#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        l = 0
        r = len(nums) - 1
        ans = []
        # 先找左边界
        while l < r:
            m = (r + l) >> 1
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        if nums[l] != target:
            return [-1, -1]
        ans.append(l)
        # 寻找右边界
        r = len(nums) - 1
        while l < r:
            m = (r + l + 1) >> 1
            if nums[m] > target:
                r = m - 1
            else:
                l = m
        ans.append(l)
        
        return ans
'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = bisect.bisect_left(nums, target)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        right = bisect.bisect(nums, target) - 1
        # right = left + bisect.bisect(nums[left:], target) - 1  # 这样写也行
        return [left, right]
'''
