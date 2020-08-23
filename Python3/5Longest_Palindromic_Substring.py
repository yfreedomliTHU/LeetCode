#https://leetcode.com/problems/longest-palindromic-substring/

# Time complexity：O(n^2)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            # odd:'aba'
            tmp = self.expand(s, i, i)
            if len(tmp) > len(ans):
                ans = tmp
            # even:'abba'
            tmp = self.expand(s, i, i+1)
            if len(tmp) > len(ans):
                ans = tmp
        return ans
    
    def expand(self, s, l, r):
        while l>=0 and r < len(s) and s[l]==s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
        
