#https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        # 左边比右边的罗马数字大就加，小就减
        hash_map = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ans = 0
        for i in range(len(s)-1):
            if hash_map[s[i]] < hash_map[s[i+1]]:
                ans -= hash_map[s[i]]
            else:
                ans += hash_map[s[i]]
                
        ans += hash_map[s[-1]]
        return ans
