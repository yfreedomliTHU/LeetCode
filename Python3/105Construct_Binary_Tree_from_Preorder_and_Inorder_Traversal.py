#https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        #递归
        #中序：左，根，右
        #前序：根，左，右
        hashmap = {x:i for i,x in enumerate(inorder)}
        n = len(preorder)
        def btree(pre_l, pre_r, in_l, in_r):
            if pre_l > pre_r:
                return None
            pre_root = pre_l
            in_root = hashmap[preorder[pre_root]]
            # build root
            root = TreeNode(preorder[pre_root])
            left_num = in_root - in_l
            root.left = btree(pre_l+1, pre_l+left_num, in_l, in_root-1)
            root.right = btree(pre_l+left_num+1, pre_r, in_root+1, in_r)
            return root
        
        return btree(0, n-1, 0, n-1)
