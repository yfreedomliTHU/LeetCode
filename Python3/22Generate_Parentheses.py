#https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        # 1backtrack
        ans = []
        def backtrack(s, l, r):
            if len(s) == 2*n:
                ans.append(''.join(s))
                return
            if l < n :
                s.append('(')
                backtrack(s, l+1, r)
                s.pop()
            if l > r:
                s.append(')')
                backtrack(s, l, r+1)
                s.pop()
        s = []   
        backtrack(s, 0, 0)
        return ans
        '''
        # 2Recurse by the length of the sequence of parentheses
        # (a)b:a,b are Parentheses
        if n==0:
            return ['']
        ans = []
        for i in range(n):
            for left in self.generateParenthesis(i):
                for right in self.generateParenthesis(n-1-i):
                    ans.append('({}){}'.format(left, right))
        return ans
