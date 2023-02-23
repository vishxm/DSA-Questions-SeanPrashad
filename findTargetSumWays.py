class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        index = len(nums) - 1
        cur_sum = 0
        self.memo = {}
        return self.dp(nums, target, index, cur_sum)
    
    def dp(self, nums, target, index, cur_sum):
        if (index, cur_sum) in self.memo:
            return self.memo[(index, cur_sum)]
        if index < 0:
            if cur_sum == target:
                return 1
            else:
                return 0
            
        positive = self.dp(nums, target, index-1, cur_sum + nums[index])
        negative = self.dp(nums, target, index-1, cur_sum-nums[index])
        self.memo[(index, cur_sum)] = positive + negative
        return self.memo[(index, cur_sum)]