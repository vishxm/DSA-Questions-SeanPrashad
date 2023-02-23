class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        left, right = 0, len(nums) - 1
        while left <= right:
            if pow(nums[left],2) > pow(nums[right],2):
                res.append(pow(nums[left],2))
                left += 1
            else:
                res.append(pow(nums[right],2))
                right -= 1
        return res[::-1]