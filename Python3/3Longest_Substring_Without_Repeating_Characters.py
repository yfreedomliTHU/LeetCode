#https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        max_len = 0
        l = 0
        for r in range(len(s)):
            if s[r] in seen and seen[s[r]] >= l:
                l = seen[s[r]] + 1
            else:
                max_len = max(max_len, r-l+1)
            seen[s[r]] = r
            
        return max_len
