class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        if sum(nums)%2: return False
        target = sum(nums)/2
        dp = set()
        dp.add(0)

        for i in range(len(nums)-1, -1, -1):
            newDP = dp.copy()
            for t in dp:
                if nums[i]+t == target: return True
                elif nums[i]+t < target:
                    newDP.add(nums[i]+t)
            dp = newDP
        
        return target in dp

        """ total_sum = sum(nums)
        if total_sum&1: 
            return False
        
        half_sum = total_sum//2
        dp = [True] + [False]*half_sum
        for num in nums:
            for j in range(half_sum, num-1, -1):
                dp[j] |= dp[j-num]
        return dp[half_sum] """