class Solution:
    def isHappy(self, n: int) -> bool:
        currnum = n
        seen = set()
        
        while currnum != 1:
            if currnum in seen:
                return False
            
            seen.add(currnum)
            sumsq = 0 
            string = str(currnum)
            
            for i in range(len(string)):
                sumsq = sumsq + (int(string[i]) * int(string[i])) 
            
            currnum = sumsq
        
        return True