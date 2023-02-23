class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return -1
        
        low, high = 0, len(nums) - 1
        while low<=high:
            while low < high and nums[low] == nums[low+1]: low += 1
            while low < high and nums[high] == nums[high-1]: high -= 1
            mid = (high+low)//2
            if target == nums[mid] or target==nums[low] or target==nums[high]:
                return True
            elif nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return False