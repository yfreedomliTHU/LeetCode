#https://leetcode.com/problems/maximal-rectangle/

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        maxS = 0
        m, n  = len(matrix), len(matrix[0])
        dp = [0]*n
        for i in range(m):
            for j in range(n):
                dp[j] = dp[j] + 1 if matrix[i][j]=='1' else 0 #按列统计柱状图
                
            maxS = max(maxS, self.maxarea(dp))
            
        return maxS
    
    def maxarea(self, heights):
        #单调栈
        if not heights:
            return 0
        n = len(heights)
        l, r = [0]*n, [n]*n
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]]>heights[i]:
                r[stack[-1]] = i
                stack.pop()
            l[i] = stack[-1] if stack else -1
            stack.append(i)
        ans = max((r[i]-l[i]-1)*heights[i] for i in range(n))
        return ans
