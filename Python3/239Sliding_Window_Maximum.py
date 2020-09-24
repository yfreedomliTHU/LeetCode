#https://leetcode.com/problems/sliding-window-maximum/

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        #1队列O(n)
        q, res = deque(), []
        for i in range(len(nums)):
            if i-k >= 0:
                res.append(nums[q[0]])
                while q and q[0]<=i-k:
                    q.popleft()
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)
        res.append(nums[q[0]])
        return res
        '''
        #2dp
        #builf left array and right array
        if not nums or k==0:
            return []
        if k == 1:
            return nums
        n = len(nums)
        left = [0]*n
        right = [0]*n
        left[0] = nums[0]
        right[n-1] = nums[n-1]
        for i in range(1, n):
            if i % k == 0:
                left[i] = nums[i]
            else:
                left[i] = max(left[i-1], nums[i])
            j = n-i-1
            if (j+1) % k ==0:
                right[j] = nums[j]
            else:
                right[j] = max(right[j+1], nums[j])
        ans = []
        for i in range(n-k+1):
            ans.append(max(right[i], left[i+k-1]))
        
        return ans
