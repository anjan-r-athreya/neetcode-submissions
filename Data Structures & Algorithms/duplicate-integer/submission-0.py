class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prev = {}

        for i in range(len(nums)):
            if nums[i] not in prev:
                prev[nums[i]] = i
            else:
                return True
        return False