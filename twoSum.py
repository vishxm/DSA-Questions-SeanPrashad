class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        res = []
        for idx, num in enumerate(nums):
            if target - num in numDict.keys():
                res.append(numDict[target - num])
                res.append(idx)
                return res
            else:
                numDict[num] = idx
        return []