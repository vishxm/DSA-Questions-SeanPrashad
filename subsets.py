class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]: 
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in xrange(index, len(nums)):
            self.dfs(nums, i+1, path+nums[i], res)
        
        """ resultList = []
        def dfs(idx, subList, mainList):
            if idx >= len(mainList):
                temp = subList.copy()
                resultList.append(temp)
                del temp
                return
            subList.append(mainList[idx])
            dfs(idx+1, subList, mainList)
            subList.pop()
            dfs(idx+1, subList, mainList)

        dfs(0, [], nums)
        return resultList """