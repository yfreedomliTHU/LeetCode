#https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        # 1.排序数组分类
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        
        return ans.values()
        '''
        # 2.按计数分类
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0]*26
            for x in s:
                count[ord(x)-ord('a')] += 1
            ans[tuple(count)].append(s)
        
        return ans.values()
            
