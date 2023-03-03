class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        charSet = {}
        res = 0
        for right in range(len(s)):
            if s[right] not in charSet:
                res = max(res, right-left+1)
            else:
                if charSet[s[right]] < left:
                    res = max(res, right-left+1)
                else:
                    left = charSet[s[right]] + 1
            charSet[s[right]] = right

        return res