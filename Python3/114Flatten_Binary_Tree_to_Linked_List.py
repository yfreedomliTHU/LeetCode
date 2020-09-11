#https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        preorder = []
        def preorderT(root):
            if root:
                preorder.append(root)
                preorderT(root.left)
                preorderT(root.right)
        preorderT(root)
        n = len(preorder)
        for i in range(1, n):
            pre, cur = preorder[i-1], preorder[i]
            pre.left = None
            pre.right = cur
            
