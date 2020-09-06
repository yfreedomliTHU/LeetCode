#https://leetcode.com/problems/minimum-window-substring/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #two pointers
        need = collections.defaultdict(int)
        for x in t:
            need[x] += 1
        needCount = len(t)
        l = 0
        tmp = (0, float('inf'))
        for r, c in enumerate(s):
            if need[c] > 0:
                needCount -= 1
            need[c] -= 1
            if needCount==0:
                while 1:
                    c = s[l]
                    if need[c]==0:
                        break
                    need[c] += 1
                    l += 1
                if r-l<tmp[1]-tmp[0]:
                    tmp = (l, r)
                need[s[l]] += 1
                needCount += 1
                l += 1
        return "" if tmp[1]>len(s) else s[tmp[0]:tmp[1]+1]
