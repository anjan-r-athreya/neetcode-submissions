class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_water = 0

        for i in range(len(height)):
            ptr1 = i
            ptr2 = i

            max_left = 0
            while ptr1 >= 0:
                if height[ptr1] > max_left:
                    max_left = height[ptr1]
                ptr1 -= 1
            
            max_right = 0
            while ptr2 < n:
                if height[ptr2] > max_right:
                    max_right = height[ptr2]
                ptr2 += 1

            water_i = min(max_left, max_right) - height[i]
            max_water += water_i
    
        return max_water

