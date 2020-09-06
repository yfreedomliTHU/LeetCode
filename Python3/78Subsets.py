#https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        #1.迭代
        ans = [[]]
        for x in nums:
            ans += [[x]+numlist for numlist in ans]
        return ans
        '''
        #2.backtrack
        ans = []
        n = len(nums)
        def backtrack(tmp, start):
            ans.append(tmp)
            for i in range(start, n):
                backtrack(tmp+[nums[i]], i+1)
        backtrack([],0)
        return ans
