#https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #单调栈
        n = len(heights)
        if n == 0:
            return 0
        l ,r = [0]*n, [n]*n
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]]>=heights[i]:
                r[stack[-1]] = i
                stack.pop()
            l[i] = stack[-1] if stack else -1
            stack.append(i)
        print(l,r)
        res = max((r[i]-l[i]-1)*heights[i] for i in range(n))
        return res
