# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.result = 0
        cache = {0:1}
        self.dfs(root, targetSum, 0, cache)
        return self.result
    
    def dfs(self, node, targetSum, curPathSum, cache):
        if not node:
            return
        curPathSum += node.val
        oldPathSum = curPathSum - targetSum
        self.result += cache.get(oldPathSum, 0)
        cache[curPathSum] = cache.get(curPathSum, 0) + 1
        
        self.dfs(node.left, targetSum, curPathSum, cache)
        self.dfs(node.right, targetSum, curPathSum, cache)
        cache[curPathSum] -= 1