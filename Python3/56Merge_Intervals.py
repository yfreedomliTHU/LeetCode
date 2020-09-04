#https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        intervals.sort()
        ans = [intervals[0]]
        for x in intervals[1:]:
            if ans[-1][1] < x[0]:
                ans.append(x)
            else:
                ans[-1][1] = max(ans[-1][1], x[1])
        return ans
