class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # LIS[k]: the length of the longest increasing subsequence ending at index k
        # n = len(nums) solve each LIS[i] where i in [0, n-1]
        # work backwards from the last index.

        if not nums or len(nums) == 0: return 0

        n = len(nums)
        lis = [1] * n # there will always be an lis of at least 1

        for k in range(n-2, -1, -1):
            for j in range(k+1, n):
                if nums[k] < nums[j]:
                    lis[k] = max(lis[k], 1 + lis[j])
        
        return max(lis)
