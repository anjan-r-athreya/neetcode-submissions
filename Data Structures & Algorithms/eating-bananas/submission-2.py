import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)

        l = 1
        r = max(piles)
        k = r

        while l <= r:
            mid = (l + r) // 2
            currHours = 0

            for i in range(n):
                currHours += math.ceil(piles[i] / mid)
            
            if currHours <= h:
                k = mid
                r = mid - 1
            elif currHours > h:
                l = mid + 1

        return k
