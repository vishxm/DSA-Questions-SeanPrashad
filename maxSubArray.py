class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        runningSum = 0
        maxi = nums[i]
        for i in range(len(nums)):
            runningSum += nums[i]
            if runningSum > maxi:
                maxi = runningSum
            if runningSum < 0:
                runningSum = 0
        return maxi