class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        inc = sorted(heights)
        n = len(heights)

        number = 0

        for i in range(n):
            if heights[i] != inc[i]: number = number + 1

        return number