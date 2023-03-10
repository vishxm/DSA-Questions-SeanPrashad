class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        target = sum(nums)
        if target%k: return False
        nums.sort(reverse=True)
        target = target/k
        used = [False]*len(nums)

        def backtrack(i, k, subSetSum):
            if k == 0: 
                return True
            if subSetSum == target:
                return backtrack(0, k-1, 0)
            
            for j in range(len(nums)):
                if used[j] or subSetSum+nums[j] > target:
                    continue
                used[j] = True
                if backtrack(j+1, k, subSetSum+nums[j]):
                    return True
                used[j] = False
            return False
        return backtrack(0, k, 0)