#https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxSum = float('-inf')
        def maxNode(node):
            if not node:
                return 0
            leftmax = max(maxNode(node.left), 0)
            rightmax = max(maxNode(node.right), 0)
            
            self.maxSum = max(self.maxSum, node.val+leftmax+rightmax)
            
            return node.val+max(leftmax, rightmax)
        
        maxNode(root)
        return self.maxSum
