# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, cur_sum):
            if node is None:
                return False
            cur_sum += node.val
            if not node.left and not node.right:
                return cur_sum == targetSum
            return dfs(node.left, cur_sum) or dfs(node.right, cur_sum)
        return dfs(root,0)


""" class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        return self.dfs(root, targetSum)
        
    def dfs(self, node, remainingSum):
        if not node:
            return False
        if not node.right and not node.left and remainingSum == node.val:
            return True
        return self.dfs(node.left, remainingSum-node.val) or self.dfs(node.right, remainingSum-node.val) """
        

""" class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def hasPathSum(self, root, sum):
            if not root:
                return False
    
            if not root.left and not root.right and root.val == sum:
                return True
            
            sum -= root.val
    
            return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum) """