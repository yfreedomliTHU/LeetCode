#https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        #递归 max(l, r)+1
        if not root:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right))+1
