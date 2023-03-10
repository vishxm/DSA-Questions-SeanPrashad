class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        size = 0
        for num in nums:
            if size==0 or num > sub[size-1]:
                sub.append(num)
                size += 1
            else:
                i = bisect_left(sub,num)
                sub[i] = num
        return len(sub)

        """ LIS = [1]*len(nums)
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1+LIS[j])
        return max(LIS) """