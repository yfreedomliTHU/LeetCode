#https://leetcode.com/problems/house-robber-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        # dp + 递归
        # max(max(左不抢,左抢)+max(右不抢，右抢)， 抢根节点+左不抢+右不抢)
        if not root:
            return 0

        def helper(node):
            if not node:
                return 0, 0
            
            l_not, l = helper(node.left)
            r_not, r = helper(node.right)
            
            return max(l_not, l)+max(r_not, r), node.val+l_not+r_not
        
        return max(helper(root))
