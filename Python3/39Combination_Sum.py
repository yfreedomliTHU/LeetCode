#https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        c_sort=sorted(candidates)
        lenth = len(c_sort)
        
        res = []
        
        def match(idx, tmp, remain):
            for i in range(idx, lenth):
                if c_sort[i] == remain:
                    res.append(tmp + [c_sort[i]])
                elif c_sort[i] < remain:
                    match(i, tmp+[c_sort[i]], remain-c_sort[i])
                elif c_sort[i] > remain:
                    return
        
        match(0, [], target)
        return res
        
