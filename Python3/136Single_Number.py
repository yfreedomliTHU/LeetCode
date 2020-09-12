#https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 异或运算符
        ans = 0
        for x in nums:
            ans ^= x
        
        return ans
