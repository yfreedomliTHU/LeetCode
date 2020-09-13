#https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        global_len = 0
        num_set = set(nums)
        for num in num_set:
            if num-1 not in num_set:
                cur_len = 1
                cur_num = num
                while cur_num+1 in num_set:
                    cur_len += 1
                    cur_num += 1
                    
                global_len = max(cur_len, global_len)
                
        return global_len
