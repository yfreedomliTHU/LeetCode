#https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {
                    '{':'}',
                    '[':']',
                    '(':')'
                    }
        stack = []
        for x in s:
            if x in hashmap:
                stack.append(x)
            elif len(stack) == 0: # considering "]"
                return False
            elif hashmap[stack.pop()]!=x:
                return False
        return len(stack) == 0  
