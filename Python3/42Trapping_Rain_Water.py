#https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        # two pointers
        if not height:
            return 0
        n = len(height)
        l, r = 0, len(height)-1
        hl , hr= height[0], height[n-1]
        ans = 0
        while l < r:
            hl = max(hl, height[l])
            hr = max(hr, height[r])
            if hl < hr:
                ans += (hl - height[l])
                l += 1
            else:
                ans += (hr - height[r])
                r -= 1
        return ans
