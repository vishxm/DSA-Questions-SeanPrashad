class Solution: # iterative DP
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        memo = [0]*(len(nums)+1)
        memo[0] = 0
        memo[1] = nums[0]
        for i in range(1, len(nums)):
            val = nums[i]
            memo[i+1] = max(memo[i], memo[i-1]+val)
        return memo[len(nums)]

""" class Solution: #memoized recursion
    def rob(self, nums: List[int]) -> int:
        memo = [-1]*(len(nums)+1)
        def dfs(nums, index):
            if index<0: 
                return 0
            if memo[index] >= 0:
                return memo[index]
            memo[index] = max(dfs(nums, index-2)+nums[index],\
                              dfs(nums, index-1))
            return memo[index]
        return dfs(nums, len(nums)-1)  """

""" class Solution: #pure recursion
    def rob(self, nums: List[int]) -> int:
        res = 0
        def dfs(nums, index, cur_sum):
            if index >= len(nums):
                return cur_sum
            return max(dfs(nums, index+2, cur_sum+nums[index]),\
                       dfs(nums, index+3, cur_sum+nums[index]))
        
        return max(dfs(nums, 0, 0), dfs(nums, 1, 0)) """