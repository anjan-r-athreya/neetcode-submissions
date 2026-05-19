class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)

        if n != m: return False

        letterS = {}
        letterT = {}

        for i in range(n):
            if s[i] not in letterS:
                letterS[s[i]] = 1
            else:
                letterS[s[i]] = letterS[s[i]] + 1

            if t[i] not in letterT:
                letterT[t[i]] = 1
            else:
                letterT[t[i]] = letterT[t[i]] + 1
            
        return letterS == letterT