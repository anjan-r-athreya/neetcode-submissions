class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in pairs:
                return [pairs[diff], i]
            
            pairs[n] = i        
