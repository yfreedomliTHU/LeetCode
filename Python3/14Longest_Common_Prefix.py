#https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        ans = ""
        if len(strs) == 0: return ""
        com_len = len(strs[0])
        for i in range(1, len(strs)):
            com_len = min(com_len, len(strs[i]))
        if com_len == 0: return ""   
        flag = 0
        for j in range(com_len):
            for i in range(1, len(strs)):
                if strs[i][j] !=strs[0][j]:
                    flag = 1
                    break
            if flag:
                break
            ans += strs[0][j]
        
        return ans
        '''
        # Compare min(strs) and max(strs)
        if len(strs) == 0: return ""
        s_min, s_max = min(strs), max(strs)
        for i in range(len(s_min)):
            if s_min[i]!=s_max[i]:
                return s_min[:i]
        
        return s_min
