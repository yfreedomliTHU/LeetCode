#https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        #递归
        if not root:
            return True
        
        return self.isBST(root, float('inf'), float('-inf'))
    def isBST(self, root, MAX, MIN):
        if not root:
            return True
        tmp = root.val
        return MIN<tmp<MAX and self.isBST(root.left, tmp, MIN) and self.isBST(root.right, MAX, tmp)
        
