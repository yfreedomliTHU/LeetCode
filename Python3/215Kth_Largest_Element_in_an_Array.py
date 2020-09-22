#https://leetcode.com/problems/kth-largest-element-in-an-array/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        tmp = sorted(nums)[::-1]
        return tmp[k-1]
        
        #快排
        def quick_sort(nums):
            if len(nums) <=1:
                return nums
            base = nums[0]
            less = [x for x in nums[1:] if x <= base]
            more = [x for x in nums[1:] if x > base]
            return quick_sort(less) + [base] + quick_sort(more)
        
        tmp = quick_sort(nums)
        return tmp[-k]
        '''
        '''
        def partition(left, right):
            pivot = nums[left]
            l = left+1
            r = right
            while l<=r:
                if nums[l] < pivot and nums[r] > pivot:
                    nums[l], nums[r] = nums[r], nums[l]
                if nums[l] >= pivot:
                    l += 1
                if nums[r] <= pivot:
                    r -= 1
            nums[r], nums[left] = nums[left], nums[r]
            return r
        left = 0
        right = len(nums) - 1
        while 1:
            idx = partition(left, right)
            if idx == k - 1:
                return nums[idx]
            if idx < k - 1:
                left = idx + 1
            if idx > k - 1:
                right = idx - 1
        '''
        def adjust_heap(idx, max_len):
            left = 2 * idx + 1
            right = 2 * idx + 2
            max_loc = idx
            if left < max_len and nums[max_loc] < nums[left]:
                max_loc = left
            if right < max_len and nums[max_loc] < nums[right]:
                max_loc = right
            if max_loc != idx:
                nums[idx], nums[max_loc] = nums[max_loc], nums[idx]
                adjust_heap(max_loc, max_len)
        
        # 建堆
        n = len(nums)
        for i in range(n // 2 - 1, -1, -1):
            adjust_heap(i, n)
        #print(nums)
        res = None
        for i in range(1, k + 1):
            #print(nums)
            res = nums[0]
            nums[0], nums[-i] = nums[-i], nums[0]
            adjust_heap(0, n - i)
        return res
