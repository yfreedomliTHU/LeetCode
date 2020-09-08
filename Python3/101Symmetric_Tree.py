#https://leetcode.com/problems/symmetric-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        #递归
        if not root: return True
        def DFS(t1, t2):
            if not t1 and not t2:
                return True
            elif not t1 or not t2:
                return False
            elif t1.val!=t2.val:
                return False
            return DFS(t1.left, t2.right) and DFS(t1.right, t2.left)
        
        return DFS(root.left, root.right)
