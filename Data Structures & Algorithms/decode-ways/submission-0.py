class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = { n : 1 }

        # two options, take one digit, take two digits
        def dfs(i):
            nonlocal n

            if i == n:
                return 1
            if s[i] == "0":
                return 0
            if i in dp:
                return dp[i]

            result = dfs(i + 1)
            
            if i + 1 < n and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
                result += dfs(i+2)
            dp[i] = result

            return result
        
        return dfs(0)

        

"""
consider increasing subsets of the input string s:

e.g input s = "1012"

- On iteration 1 there will always be only one way to decode it, unless it = 0
iteration 1:
subset = "1"
"1" -> 'A'
decodings = [1,1,1,1]

iteration 2:
subset = "10"

"""