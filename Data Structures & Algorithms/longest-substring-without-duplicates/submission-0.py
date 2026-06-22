class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window + hashmap for counting occurences
        n = len(s)
        longest = 1

        for i in range(n):
            hashmap = {}
            end = i

            while end < n and s[end] not in hashmap:
                hashmap[s[end]] = 1
                end += 1

            longest = max(longest, end - i)

        return longest