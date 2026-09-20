class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix sum and postfix sum

        if not nums: return None
        n = len(nums)

        # build prefix arr
        prefix = [1] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        # build postfix arr
        postfix = [1] * (n + 1)
        for i in range(n - 1, -1, -1):
            postfix[i] = postfix[i+1] * nums[i]

        result = [0] * n

        for i in range(n):
            result[i] = prefix[i] * postfix[i+1]
        
        return result


"""
nums = [1,2,4,6]

prefix  = [0, 1, 3, 7,13]
postfix = [13,12,10,6,0]

prefix:   [1,  1,  2,  8, 48]
postfix:  [48, 48, 24, 6, 1]
          []
"""