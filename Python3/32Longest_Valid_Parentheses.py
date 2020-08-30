#https://leetcode.com/problems/longest-valid-parentheses/

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        '''
        一、入栈条件为1.栈为空 2.当前字符是'(' 3.栈顶符号位')'，因为三种条件都没办法消去成对的括号。
        二、计算结果：符合消去成对括号时，拿当前下标减去栈顶下标即可
        '''
        if len(s) <2: return 0
        tmp = []
        lenth = 0
        for i in range(len(s)):
            if not tmp or s[i] == '(' or s[tmp[-1]]==')':
                tmp.append(i)
            else:
                tmp.pop()
                lenth = max(lenth, i - (tmp[-1] if tmp else -1))
        return lenth
