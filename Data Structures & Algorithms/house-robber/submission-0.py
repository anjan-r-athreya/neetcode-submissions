class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if not nums: return 0
        if len(nums) == 1: return nums[0]

        costs = [-1] * n
        costs[0] = nums[0]
        costs[1] = max(nums[0], nums[1])

        for i in range(2, n):
            costs[i] = max(costs[i - 1], nums[i] + costs[i - 2])
        
        return max(costs)