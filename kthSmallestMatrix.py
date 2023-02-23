class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        
        def countLessOrEqual(x):
            cnt = 0
            c = n - 1
            for r in range(m):
                while c >= 0 and matrix[r][c] > x:
                    c -= 1
                cnt += (c+1)
            return cnt

        left, right = matrix[0][0], matrix[-1][-1]
        ans = -1
        while left <= right:
            mid = (left+right)//2
            if countLessOrEqual(mid) >= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
        
        """ # heap 
        m, n = len(matrix), len(matrix[0])
        minHeap = []
        for r in range(min(k,m)):
            heappush(minHeap, (matrix[r][0], r, 0))

        ans = -1
        for i in range(k):
            ans, r, c = heappop(minHeap)
            if c+1 < n:
                heappush(minHeap, (matrix[r][c+1], r, c+1))
        return ans """