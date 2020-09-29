#https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # Double pointer O(n)
        '''
        1、一个指针从左往右寻找上界
        2、一个指针从右往左寻找下界
        '''
        size = len(nums)
        if size <= 1:
            return 0

        left = size - 2
        right = 1
        cur_min = nums[-1]
        cur_max = nums[0]
        up = 0
        down = 1

        # 由于两个指针迭代的步数是相同的，所以没必要分两次循环，在一次循环里同时移动两次指针即可。
        while left >= 0 and right < size:
            if nums[left] > cur_min:
                down = left
            else:
                cur_min = nums[left]
            if nums[right] < cur_max:
                up = right
            else:
                cur_max = nums[right]
            left -= 1
            right += 1

        return up - down + 1
