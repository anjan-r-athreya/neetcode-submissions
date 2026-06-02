class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        ptr1 = 0
        ptr2 = n - 1
        currentmax = 0

        while ptr1 < ptr2:
            current = min(heights[ptr1], heights[ptr2]) * (ptr2 - ptr1)
            if current > currentmax:
                currentmax = current
            
            if heights[ptr1] <= heights[ptr2]:
                ptr1 += 1
            elif heights[ptr1] > heights[ptr2]:
                ptr2 -= 1
        
        return currentmax