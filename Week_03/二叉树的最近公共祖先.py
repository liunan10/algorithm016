#所有节点的值都是唯一的。
#p、q 为不同节点且均存在于给定的二叉树中。
#subproblem: p and q need to be in the left and right of the common ancestor

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q: return root 
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left and not right: return None
        if not left: return right
        if not right: return left
        return root 

