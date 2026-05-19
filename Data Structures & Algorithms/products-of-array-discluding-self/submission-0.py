class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # compute prefix sum and postfix sums
        n = len(nums)
        output = [0] * n

        prefix = [0] * n
        prefix[0] = 1

        postfix = [0] * n
        postfix[-1] = 1

        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(n - 2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i+1]

        for i in range(n):
            output[i] = prefix[i] * postfix[i]
        return output

        
        
        """
        nums = [1,2,4,6]
        Output = [48,24,12,8]

        prefix  = [1,  2, 8,48]
        postfix = [48,48,24, 6]

        if we go through original nums one by one we then do
        something with prefix[0:i] and postfix[i+1:]
        """