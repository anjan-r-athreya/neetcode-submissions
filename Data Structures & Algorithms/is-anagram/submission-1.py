class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = {}
        hash2 = {}
        n1 = len(s)
        n2 = len(t)

        if n1 != n2: return False

        for i in range(n1):
            if s[i] not in hash1: hash1[s[i]] = 1
            else: hash1[s[i]] += 1

            if t[i] not in hash2: hash2[t[i]] = 1
            else: hash2[t[i]] += 1
        
        if hash1 == hash2: return True
        return False