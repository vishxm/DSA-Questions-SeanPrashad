class Solution:
    def trap(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        maxi, maxj = 0, 0
        res = 0
        while i <= j:
            if height[i] <= height[j]:
                if height[i] >= maxi:
                    maxi = height[i]
                else:
                    res += maxi-height[i]
                i += 1
            else:
                if height[j] >= maxj:
                    maxj = height[j]
                else:
                    res += maxj-height[j]
                j -= 1
        
        return res