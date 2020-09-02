#https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # backtrack
        ans = []
        def backtrack(rest, tmp):
            if not rest:
                ans.append(tmp)
                return
            for i in range(len(rest)):
                backtrack(rest[:i]+rest[i+1:], tmp+[rest[i]])
        tmp = []       
        backtrack(nums, tmp)
        return ans
