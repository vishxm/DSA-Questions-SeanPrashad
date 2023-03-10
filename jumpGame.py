class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #greedy
        last = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if i + nums[i] >= last:
                last = i
        return last <= 0
        
        """ 
        # DP
        dp = [False]*len(nums)
        dp[0] = True
        for i in range(1,len(nums)):
            for j in range(i-1,-1,-1):
                if dp[j] and nums[j] >= i-j:
                    dp[i] = True
                    break
        return dp[-1] """