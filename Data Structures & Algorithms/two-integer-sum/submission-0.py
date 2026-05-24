class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        # n is index, c is value
        for n, c in enumerate(nums):
            complement = target - c

            if complement not in prevMap:
                prevMap[c] = n
            else:
                return [prevMap[complement], n]
        
        return []
            