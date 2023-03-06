# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        prev = -math.inf
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right
        return True

        """ def helper(node, lo, hi):
            if node is None:
                return True
            if node.val <= lo or node.val >= hi:
                return False
            return helper(node.left, lo, node.val) and helper(node.right, node.val, hi)
        return helper(root, -math.inf, math.inf) """