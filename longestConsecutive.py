class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsAvailable = set(nums)
        res = 1
        for num in nums:
            if num not in numsAvailable:
                continue
            numsAvailable.remove(num)
            next = num + 1
            prev = num - 1
            while prev in numsAvailable:
                prev -= 1
            while next in numsAvailable:
                next += 1
            res = max(res, next - prev - 1)

        return res if len(nums) >= 1 else 0 