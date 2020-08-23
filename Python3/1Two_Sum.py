#https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            rest = target - nums[i]
            if rest in seen:
                return [seen[rest], i]
            seen[nums[i]] = i
            
