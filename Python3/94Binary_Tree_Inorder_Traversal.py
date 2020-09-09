#https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        '''
        #1.递归
        ans = []
        def helper(r):
            if not r:
                return
            helper(r.left)
            ans.append(r.val)
            helper(r.right)
        helper(root)   
        return ans
        '''
        #2.迭代
        ans = []
        if not root:
            return
        stack = []
        p = root
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            p = stack.pop()
            ans.append(p.val)
            p = p.right
            
        return ans
