class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for c in s:
            d[c] = d.get(c,0) + 1
        d2 = {}
        for i,j in d.items():
            if j not in d2:
                d2[j] = []
            d2[j].append(i)
        for i, _ in d2.items():
            d2[i].sort()
        ans = ''
        for i in sorted(d2.keys())[::-1]:
            for j in d2[i]:
                for _ in range(i):
                    ans += j
        return ans
