# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isMatch(self, r1, r2):
        if not(r1 and r2):
            return r1 is r2
        return (r1.val == r2.val and self.isMatch(r1.left, r2.left) and self.isMatch(r1.right, r2.right))
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.isMatch(root, subRoot):
            return True
        if not root:
            return False
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    