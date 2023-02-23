""" class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        shouldBeSum = n*(n-1)/2
        isSum = 0
        for num in nums: isSum += num
        return isSum - shouldBeSum """

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            idx = abs(num)
            if nums[idx] < 0:
                return idx
            nums[idx] = -nums[idx]
        return len