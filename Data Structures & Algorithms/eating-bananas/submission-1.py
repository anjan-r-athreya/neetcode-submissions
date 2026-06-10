import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        l = 1
        r = max(piles)
        final_k = 0

        while l <= r:
            k = (l+r) // 2

            currentHours = 0
            for i in range(n):
                currentHours += math.ceil(piles[i] / k)
            
            if currentHours <= h:
                r=k-1
                final_k = k
            elif currentHours > h:
                l=k+1
        return final_k

        

"""
binary search for the target where min(bana/hour) is the target
binary search not on the array this time
binary search on an "array" from 1 to h
"""