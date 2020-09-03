#https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 贪心算法
        n = len(nums)
        pos = 0
        for i in range(n):
            if pos >= i:
                pos = max(pos, i+nums[i])
            else:
                return False
        
        return True
