class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums: return
        pivot = random.choice(nums)
        right = [x for x in nums if x > pivot]
        mid = [x for x in nums if x == pivot]
        left = [x for x in nums if x < pivot]

        R, M = len(right), len(mid)

        if k <= R:
            return self.findKthLargest(right, k)
        elif k > R + M:
            return self.findKthLargest(left, k - R - M)
        else:
            return mid[0]

        """ heap = []
        for num in nums:
            if len(heap) == k:
                heappushpop(heap, num)
            else:
                heappush(heap, num)
        return heappop(heap) """