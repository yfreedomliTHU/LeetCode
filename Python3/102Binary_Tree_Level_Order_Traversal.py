#https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 递归
        ans = []
        if not root:
            return []
        def add_node(level, root):
            if level + 1 > len(ans):
                ans.append([])
            ans[level].append(root.val)
            if root.left:
                add_node(level+1, root.left)
            if root.right:
                add_node(level+1, root.right)
        
        add_node(0, root)
        return ans
