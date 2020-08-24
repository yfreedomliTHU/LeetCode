#https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, str: str) -> int:
        
        s = str.strip()
        print(s)
        if len(s) == 0: return 0
        sign = -1 if s[0]=='-' else 1
        if s[0] in ['+', '-']: s=s[1:] # need to remove sign after judge
        
        result = 0
        for i in range(len(s)):
            if s[i].isdigit():
                result = result*10 + int(s[i])
            else:
                break
        INT_MAX = 2**31-1
        INT_MIN = -2**31
        return max(INT_MIN, min(result*sign, INT_MAX))
        
