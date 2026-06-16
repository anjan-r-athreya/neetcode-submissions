class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 1
        n = len(s)

        if n == 1: return 1
        if not s: return 0

        bound1 = 0
        bound2 = 1 # bound not included
        hashset = set()
        hashset.add(s[0])

        while bound1 < n and bound2 < n:

            while s[bound2] in hashset:
                hashset.remove(s[bound1])
                bound1 += 1

            hashset.add(s[bound2])
            current = bound2 - bound1 + 1

            if current > longest: longest = current
            bound2 += 1

        return longest