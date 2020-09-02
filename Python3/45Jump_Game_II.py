#https://leetcode.com/problems/jump-game-ii/

class Solution:
    def jump(self, nums: List[int]) -> int:
        # 贪心算法
        n = len(nums)
        pos, end, step = 0, 0, 0
        for i in range(n-1):
            if pos >= i:
                pos = max(pos, i+nums[i])
                if i == end:
                    end = pos
                    step += 1
                    
        return step
