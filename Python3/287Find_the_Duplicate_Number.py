#https://leetcode.com/problems/find-the-duplicate-number/


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) # [1, n-1]
        l = 1
        r = n - 1
        while l < r:
            mid = l + (r - l) // 2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            #抽屉原理：小于mid的数个数大于mid,则重复的数一定位于[1, mid]
            if count > mid:
                r = mid
            else:
                l = mid + 1
        return l
