class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sqr = []
        n = len(nums)

        ptr1 = 0
        ptr2 = n-1

        while ptr1 <= ptr2:
            sqr1 = nums[ptr1] ** 2
            sqr2 = nums[ptr2] ** 2

            if sqr1 > sqr2:
                sqr.append(sqr1)
                ptr1 += 1
            elif sqr1 < sqr2:
                sqr.append(sqr2)
                ptr2 -= 1
            else:
                sqr.append(sqr1)
                sqr.append(sqr2)
                ptr1 += 1
                ptr2 -= 1
        
        return list(reversed(sqr[0:n]))