class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for i in range(n)]
        longest = ""

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                
                if i == j:
                    dp[i][j] = True
                elif s[i] == s[j] and j - i <= 2:
                    dp[i][j] = True
                elif s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True

                if dp[i][j]:
                    if j - i + 1 > len(longest):
                        longest = s[i:j+1]
        
        return longest
        