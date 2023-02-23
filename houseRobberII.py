class Solution:
    def rob(self, nums: List[int]) -> int:
        res = 0
        memo = [-1]*(len(nums)+1)
        memo[0] = 0
        def dp(nums, index, cur_sum):
            if index >= len(nums):
                return cur_sum
            if memo[index] >= 0:
                return memo[index]
            memo[index] = max(dp(nums, index+2, cur_sum+nums[index]),\
                              dp(nums, index+3, cur_sum+nums[index]))
            return memo[index]
        first_pick = dp(nums, 0, 0)
        memo = [-1]*(len(nums)+1)
        memo[0] = 0
        second_pick = dp(nums[1:-1], 0, 0)
        return max(first_pick, second_pick)