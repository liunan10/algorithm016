# recursion method
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.helper(root, res)
        return res 
    
    def helper(self, node, res):
        if not node:
            return
        
        res.append(node.val)
        self.helper(node.left, res)
        self.helper(node.right, res)

#iterative method. pop, store val, save right, save left
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        res = []
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res

