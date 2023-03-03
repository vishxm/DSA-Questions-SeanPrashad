class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        cntr = Counter(nums)
        for d,v in cntr:
            heappush(heap, (v,d))
        while len(heap) > k:
            heappop(heap)
        return [d for v,d in heap]