class Solution:

    def encode(self, strs: List[str]) -> str:
        n = len(strs)

        for i in range(n):
            currlen = len(strs[i])

            strs[i] = "#" + str(currlen) + strs[i]
        
        return ''.join(strs)

    def decode(self, s: str) -> List[str]:

        n = len(s)
        words = []

        i = 0

        while i < n and s[i] == "#":
            currlen = ""

            if s[i+1].isnumeric():
                j = i + 1
                
                while j < n and s[j].isnumeric():
                    currlen += s[j]
                    j += 1
            
            words.append(s[i + 1 + len(currlen):i + 1 + len(currlen) + int(currlen)])
            i = i + 1 + len(currlen) + int(currlen)
        
        return words
        

