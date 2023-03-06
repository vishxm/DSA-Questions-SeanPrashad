class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        minTillNow = float('inf')
        sumOfMin = 0
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            low, high = i+1, len(nums)-1
            while low<high:
                tempSum = nums[i] + nums[low] + nums[high]
                if abs(target-tempSum) < minTillNow:
                    minTillNow = abs(target-tempSum)
                    sumOfMin = tempSum
                if tempSum > target:
                    high -= 1
                elif tempSum <= target:
                    low += 1
        return sumOfMin
