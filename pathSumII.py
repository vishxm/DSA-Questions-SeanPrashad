# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        ans = []
        def helper(node, path, curSum):
            if curSum == targetSum and not(node.left or node.right):
                ans.append(path)
                return
            if node.left:
                helper(node.left, path+[node.left.val], curSum+node.left.val)
            if node.right:
                helper(node.right, path+[node.right.val], curSum+node.right.val)
        helper(root, [root.val], root.val)
        return ans