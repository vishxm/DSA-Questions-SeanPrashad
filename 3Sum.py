class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, num in enumerate(nums):
            if i>0 and num == nums[i-1]:
                continue
            low, high = i + 1, len(nums) - 1
            while low < high:
                threeSum = num + nums[low] + nums[high]
                if threeSum > 0 :
                    high -= 1
                elif threeSum < 0 :
                    low += 1
                else:
                    res.append([num, nums[low], nums[high]])
                    low += 1
                    while nums[low] == nums[low -1] and low < high:
                        low += 1
        return res