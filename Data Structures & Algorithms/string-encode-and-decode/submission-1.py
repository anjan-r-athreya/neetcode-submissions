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
            length = ""

            if s[i] == "#":
                i += 1

                while i < n and s[i].isnumeric(): 
                    length += s[i]
                    i += 1
                
                strs.append(s[i : i + int(length)])

                i = i + int(length)
            else: i = i + 1
        return strs