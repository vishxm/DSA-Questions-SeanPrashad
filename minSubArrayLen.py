class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # lee's code
        i, res = 0, len(nums)+1
        for j in range(len(nums)):
            target -= nums[j]
            while target <= 0:
                res = min(res, j-i+1)
                target += nums[i]
                i += 1
        return res%(len(nums)+1)
        
        """ left, right = 0, 0
        minLength = len(nums) + 1
        intermediateSum = nums[0]
        while left <= right < len(nums):
            if intermediateSum >= target:
                minLength = min(minLength, right-left+1)
                intermediateSum -= nums[left]
                left += 1
            else:
                right += 1
                if right < len(nums): intermediateSum += nums[right]
        if minLength == len(nums) + 1:
            return 0
        return minLength """