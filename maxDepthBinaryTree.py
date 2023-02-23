# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def dfs(node, counter):
            if not node:
                return counter
            return max(dfs(node.left, counter+1), dfs(node.right, counter+1))

        return dfs(root, 0)