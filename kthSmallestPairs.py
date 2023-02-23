class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        m, n, visited = len(nums1), len(nums2), set()
        if m == 0 or n == 0: return []
        heap = [(nums1[0]+nums2[0], (0, 0))]
        for _ in range(min(k, m*n)):
            val, (i, j) = heappop(heap)
            res.append([nums1[i], nums2[j]])
            if i+1 < m and (i+1, j) not in visited:
                heappush(heap, (nums1[i+1]+nums2[j], (i+1, j)))
                visited.add((i+1, j))
            if j+1 < n and (i, j+1) not in visited:
                heappush(heap, (nums1[i]+nums2[j+1], (i, j+1)))
                visited.add((i, j+1))
        return res


""" class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2: return []
        visited, heap, output = [], [], []

        heappush(heap, (nums1[0]+nums2[0], 0, 0))
        visited.append((0,0))

        while len(output) < k and heap:
            theSum, pos1, pos2 = heappop(heap)
            output.append((nums1[pos1], nums2[pos2]))

            if pos1 + 1 < len(nums1) and (pos1+1, pos2) not in visited:
                heappush(heap, (nums1[pos1+1]+nums2[pos2], pos1+1, pos2))
                visited.append((pos1+1, pos2))
            if pos2 + 1 < len(nums2) and (pos1, pos2+1) not in visited:
                heappush(heap, (nums1[pos1]+nums2[pos2+1], pos1, pos2+1))
                visited.append((pos1, pos2+1))

        return output """