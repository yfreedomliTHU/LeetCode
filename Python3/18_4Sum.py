#https://leetcode.com/problems/4sum/

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def findNsum(l, r, target, N, result, results):
            if r-l+1 < N or N < 2 or target < nums[l]*N or target > nums[r]*N:  
                return []
            # early termination
            if N == 2: # two pointers solve sorted 2-sum problem
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        # jump to next different number
                        l0 = l + 1
                        while l0 < r and nums[l] == nums[l0]:
                            l0 += 1
                        l = l0
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
                    
            else: # recursively reduce N
                for i in range(l, r+1):
                    if i == l or (i > l and nums[i-1] != nums[i]):
                        findNsum(i+1, r, target-nums[i], N-1, result+[nums[i]], results)

        nums.sort()
        results = []
        result = []
        findNsum(0, len(nums)-1, target, 4, result, results)
        return results
