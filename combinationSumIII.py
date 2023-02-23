class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        self.dfs(range(1,10), k, n, 0, [], res)
        return res
    
    def dfs(self, nums, k, target, index, path, res):
        """ if k == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            self.dfs(nums, k-1, i+1, path+[nums[i]], res) """
        if k == 0 and target == 0:
            res.append(path)
            return
        if k < 0 or target < 0:
            return
        for i in range(index, len(nums)):
            self.dfs(nums, k-1, target-nums[i], i+1, path+[nums[i]], res)