class Solution:

    def encode(self, strs: List[str]) -> str:
        lengths = []
        n = len(strs)

        for i in range(n):
            curr = len(strs[i])
            strs[i] = "#" + str(curr) + strs[i]

        return ''.join(strs)
        
    def decode(self, s: str) -> List[str]:
        n = len(s)
        strs = []

        i = 0

        while i < n:
            if s[i] == "#":
                strs.append(s[i+2 : i+2 + int(s[i+1])])

                i = i + 2 + int(s[i+1])
        return strs