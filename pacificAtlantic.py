class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights: return
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m = len(heights)
        n = len(heights[0])
        pacific = [[False for _ in range(n)] for _ in range(m)]
        atlantic = [[False for _ in range(n)] for _ in range(m)]
        res = []

        def dfs(ocean, i, j):
            ocean[i][j] = True
            for di, dj in directions:
                ni, nj = i+di, j+dj
                if ni<0 or nj<0 or ni>= m or nj >= n or ocean[ni][nj] or heights[ni][nj] < heights[i][j]:
                    continue
                dfs(ocean, ni, nj)

        for i in range(m):
            dfs(pacific, i, 0)
            dfs(atlantic, i, n-1)
        for j in range(n):
            dfs(pacific, 0, j)
            dfs(atlantic, m-1, j)
        for i,j in product(range(m), range(n)):
            if atlantic[i][j] and pacific[i][j]:
                res.append([i,j])
        return res