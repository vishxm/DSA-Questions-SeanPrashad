class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if n*m != len(original):
            return []
        res = []
        idx = 0
        for i in range(m):
            res.append(original[idx:idx+n])
            idx += n
        return res