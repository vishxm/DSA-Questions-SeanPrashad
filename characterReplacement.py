class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        c_frequency = {}
        res = 0
        for right in range(len(s)):
            c_frequency[s[right]] = c_frequency.get(s[right],0) + 1
            totalChars = right - left + 1
            if totalChars - max(c_frequency.values()) <= k:
                res = max(res, totalChars)
            else:
                c_frequency[s[left]] -= 1
                if not c_frequency[s[left]]: c_frequency.pop(s[left])
                left += 1
        return res