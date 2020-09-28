#https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        #DFS
        if not root:
            return 0
        self.ans = 0
        def dfs(node):
            if not node:
                return 0
            L = dfs(node.left)
            R = dfs(node.right)
            self.ans = max(self.ans, L+R)
            return max(L, R) + 1
        
        dfs(root)
        return self.ans
