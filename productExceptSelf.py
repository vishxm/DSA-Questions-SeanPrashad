class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCount = 0
        for num in nums:
            if num == 0:
                zeroCount += 1
        
        res = [0]*len(nums)

        if zeroCount > 1:
            return res
        
        if zeroCount == 1:
            temp = 1
            for num in nums:
                if num != 0:
                    temp *= num
            for idx, num in enumerate(nums):
                if num == 0:
                    res[idx] = temp

        else:
            temp = 1
            for num in nums:
                temp *= num
            
            for idx, num in enumerate(nums):
                res[idx] = int(temp/num)
        
        return res