#https://leetcode.com/problems/word-break/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[j] = dp[i]&[i:j]
        n = len(s)
        dp = [0]*(n+1)
        dp[0] = 1
        for i in range(n):
            for j in range(i+1, n+1):
                if dp[i]==1 and s[i:j] in wordDict:
                    dp[j] = 1
                    
        return dp[-1]==1
