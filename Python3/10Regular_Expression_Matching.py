# https://leetcode.com/problems/regular-expression-matching/

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        import re
        i = re.match(p, s)
        return True if i and i.group() == s else False
        '''
        # DP Solution
        '''
        If dp[i][j] == False, it means s[:i] doesn't match p[:j]
        If dp[i][j] == True, it means s[:i] matches p[:j]
        '.' Matches any single character.
        '*' Matches zero or more of the preceding element.
        s = "aa"
        p = "a*"
        Output: true
        Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by        repeating 'a' once, it becomes "aa".
        '''
        '''
        我们不妨换个角度考虑这个问题：字母 + 星号的组合在匹配的过程中，本质上只会有两种情况：

        1.匹配 ss 末尾的一个字符，将该字符扔掉，而该组合还可以继续进行匹配；

        2.不匹配字符，将该组合扔掉，不再进行匹配。

        '''
        len_s = len(s)
        len_p = len(p)
        
        def match(i, j):
            if i == 0: return False
            if p[j-1] == '.':
                return True
            return s[i-1] == p[j-1]
        
        dp = [[False] * (len_p+1) for _ in range(len_s+1)]
        dp[0][0] = True
        for i in range(len_s+1):
            for j in range(1, len_p+1):
                if p[j-1] == '*':
                    if match(i, j-1):
                        dp[i][j] = dp[i][j-2] or dp[i-1][j]
                    else:
                        dp[i][j] = dp[i][j-2]
                else:
                    if match(i,j):
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = False
        
        return dp[-1][-1]
