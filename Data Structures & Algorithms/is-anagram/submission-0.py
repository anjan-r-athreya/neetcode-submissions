class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count = {}
        t_count = {}

        for i in range(len(s)):
            if s[i] not in s_count:
                s_count[s[i]] = 1
            elif s[i] in s_count:
                s_count[s[i]] += 1

            if t[i] not in t_count:
                t_count[t[i]] = 1
            elif t[i] in t_count:
                t_count[t[i]] += 1

        if s_count != t_count:
            return False
        
        return True