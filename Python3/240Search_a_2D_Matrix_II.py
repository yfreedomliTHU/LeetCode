#https://leetcode.com/problems/search-a-2d-matrix-ii/

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        '''
        #DFS
        #Time Limit Exceeded
        if not matrix:
            return False
        def dfs(matrix, i, j, target):
            m = len(matrix)
            n = len(matrix[0])
            if 0<=i<m and 0<=j<n:
                if matrix[i][j] == target:
                    return True
                elif matrix[i][j] < target:
                    return dfs(matrix, i+1, j, target) or dfs(matrix, i, j+1, target)
            return False
        
        return dfs(matrix, 0, 0, target)
        '''
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        row, col = m - 1, 0
        while row >= 0 and col < n:
            if matrix[row][col] < target:
                col += 1
            elif matrix[row][col] > target:
                row -= 1
            else:
                return True
        return False
