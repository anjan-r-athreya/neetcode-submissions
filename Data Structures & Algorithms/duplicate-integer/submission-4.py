class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}

        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]] = True
            elif nums[i] in seen:
                return True
        
        return False