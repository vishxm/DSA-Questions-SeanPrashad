class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix 
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
        
        """ 
        DIVISION OPERATOR IS NOT TO BE USED
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
        
        return res """