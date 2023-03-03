class Solution:
    def reorganizeString(self, s: str) -> str:
        if not s: return ""
        d = {}
        for c in s:
            d[c] = d.get(c,0) + 1
        
        h = []
        for k in d:
            heappush(h, (-d[k], k))
        
        res = ""

        while len(h) > 1:
            f1, c1 = heappop(h)
            f2, c2 = heappop(h)

            res += c1
            res += c2

            if abs(f1) > 1:
                heappush(h, (f1+1, c1))
            if abs(f2) > 1:
                heappush(h, (f2+1, c2))

        if h:
            f, c = h[0]
            if abs(f) > 1:
                return ""
            else:
                res += c
        return res
