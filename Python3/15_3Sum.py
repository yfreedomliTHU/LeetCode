#https://leetcode.com/problems/3sum/

'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # O(N^2)
        nums.sort()
        n = len(nums)
        ans = []
        
        #enumunate a
        #idx:a(i),b(j),c(k)
        for i in range(n):
            # keep different
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            target = -nums[i]
            # a+b+c=0 -> b+c=-a=target
            # enumunate c from the last
            k = n-1
            # enumunate b
            for j in range(i+1, n):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                while j < k and nums[j]+nums[k]>target:
                    k -= 1
                if j == k or nums[j]>target/2 : break
                
                if nums[j] + nums[k] == target:
                    ans.append([nums[i], nums[j],nums[k]])
        
        return ans
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        counter = collections.Counter(nums)
        nums = sorted(counter)
        ret = []
        for i, num in enumerate(nums):
            # case i. three numbers are the same - [0,0,0]
            if num==0:
                if counter[num] > 2:
                    ret.append([0, 0, 0])
            # case ii. two numbers are the same
            elif counter[num] > 1 and -2 * num in counter:
                ret.append([num, num, -2 * num])
            # case iii. not any of the three numbers are the same
            if num < 0:
                opposite = -num
                left = bisect_left(nums, opposite - nums[-1], i + 1)
                right = bisect_right(nums, opposite / 2, left)
                for a in nums[left:right]:
                    b = opposite - a
                    if b in counter and a!=b:
                        ret.append([num, a, b])
        return ret
