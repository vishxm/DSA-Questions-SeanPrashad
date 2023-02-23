class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        i, j = 0, 0
        while i < len(firstList) and j < len(secondList):
            a_start, a_end = firstList[i]
            b_start, b_end = secondList[j]
            if a_start <= b_end and b_start <= a_end:
                res.append([max(a_start,b_start), min(a_end, b_end)])
            if a_end <= b_end:
                i += 1
            else:
                j += 1
        return res