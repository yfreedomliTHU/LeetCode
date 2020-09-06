#https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #DFS
        if not board:
            return False
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if self.dfs(board, word, i, j):
                    return True
        return False
    
    def dfs(self, board, word, i, j):
        if len(word)==0:
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
            return False
        # begain search:
        tmp = board[i][j]
        board[i][j] = '0'
        result = self.dfs(board, word[1:], i+1, j) or self.dfs(board, word[1:], i, j+1) or self.dfs(board, word[1:], i-1, j) or self.dfs(board, word[1:], i, j-1)
        board[i][j] = tmp
        return result
