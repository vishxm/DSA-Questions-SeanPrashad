from heapq import *
class Solution:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        res = []
        oddEvenFlag = (k%2==1)
        small, large = [], []
        i = 0
        while i < len(nums):
            if len(small) + len(large) < k:
                num, idx = heappushpop(large, (num, i))
                heappush(small, (-num, i))
                if len(large) < len(small):
                    num, idx = heappop(small)
                    heappush(large, (-num, idx))
                i += 1
            else:
                while small and small[0][1] <= i:
                    heappop(small)
                while large and large[0][1] <= i:
                    heappop(large)
        return res