#https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        #two pointers
        # S[i][j] = min(h[i],h[j]) * (j-i)
        # max_S = max(max_S, S[i][j])
        l, r, max_S = 0, len(height)-1, 0
        while l < r:
            if height[l] < height[r]:
                max_S = max(max_S, height[l]*(r-l))
                l += 1
            else:
                max_S = max(max_S, height[r]*(r-l))
                r -= 1
        return max_S
