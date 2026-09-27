class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        if not nums or len(nums) == 0: return 0

        n = len(nums)
        lis = [1] * n # there will always be an lis of at least 1

        for k in range(n-2, -1, -1):
            for j in range(k+1, n):
                if nums[k] < nums[j]:
                    lis[k] = max(lis[k], lis[j] + 1)

        return max(lis)
