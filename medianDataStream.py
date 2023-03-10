from heapq import *
class MedianFinder:

    def __init__(self):
        self.heaps = [],[]

    def addNum(self, num: int) -> None:
        small, large = self.heaps
        heappush(small, -heappushpop(large, num))
        if len(large) < len(small):
            heappush(large, -heappop(small))

    def findMedian(self) -> float:
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        return (large[0]-small[0])/2.0
        

""" class MedianFinder:

    def __init__(self):
        self.arr = []
        self.size = 0

    def addNum(self, num: int) -> None:
        if self.size==0:
            self.arr.append(num)
        else:
            idx = bisect_left(self.arr, num)
            self.arr.insert(idx, num)
        self.size += 1

    def findMedian(self) -> float:
        if self.size%2:
            return self.arr[self.size//2]
        else:
            return (self.arr[self.size//2]+self.arr[self.size//2-1])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian() """