#https://leetcode.com/problems/3sum-closest/

'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # two pointers
        nums.sort()
        n = len(nums)
        ans = sum(nums[:3])
        for i in range(n-2):
            # ensure different
            if i>0 and nums[i]==nums[i-1]:
                continue
            j, k = i+1, n-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return s
                if abs(s-target) < abs(ans-target):
                    ans = s
                    
                if s < target:
                    # move to next different num
                    j1 = j+1
                    while j1<k and nums[j]==nums[j1]:
                        j1 += 1
                    j = j1
                else:
                    k1 = k-1
                    while k1>j and nums[k] == nums[k1]:
                        k1 -= 1
                    k = k1
                    
        return ans
'''
# k_sum not only for 3
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        return self.KSumClosest(nums, 3, target)

    def KSumClosest(self, nums: List[int], k: int, target: int) -> int:
        N = len(nums)
        if N == k:
            return sum(nums[:k])

        # target too small
        current = sum(nums[:k])
        if current >= target:
            return current

        # target too big
        current = sum(nums[-k:])
        if current <= target:
            return current
        
        if k == 1:
            return min([(x, abs(target - x)) for x in nums], key = lambda x: x[1])[0]

        closest = sum(nums[:k])
        for i, x in enumerate(nums[:-k+1]):
            if i>0 and x == nums[i-1]:
                continue
            current = self.KSumClosest(nums[i+1:], k-1, target - x) + x
            if abs(target - current) < abs(target - closest):
                if current == target:
                    return target
                else:
                    closest = current

        return closest
