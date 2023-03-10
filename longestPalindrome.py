class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestPalString = ''
        dp = [[0]*len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
            longestPalString = s[i]
        
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    if j-i==1 or dp[i+1][j-1]:
                        dp[i][j] = True
                        if len(longestPalString) < len(s[i:j+1]):
                            longestPalString = s[i:j+1]
        
        return longestPalString