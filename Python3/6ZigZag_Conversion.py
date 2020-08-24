#https://leetcode.com/problems/zigzag-conversion/


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        ans = ["" for _ in range(numRows)]
        i , flag = 0, -1
        for x in s:
            ans[i] += x
            if i ==0 or i == numRows-1:
                flag *= -1
            i += flag
            
        return "".join(ans)
        
