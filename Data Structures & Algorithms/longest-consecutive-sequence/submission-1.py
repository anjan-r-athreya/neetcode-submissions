class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0

        nums = sorted(set(nums))
        n = len(nums)

        output = -1
        count = 0
        prev = None
        for i in range(n):
            if prev == None: 
                count = 1
                prev = nums[i]
            elif nums[i] == prev + 1: 
                count += 1
                prev = nums[i]
            else: 
                output = max(count, output)
                prev = nums[i]
                count = 1
        return max(output, count)

"""
hashmap of sequences
array of sequences
sort first

[2,20,4,10,3,4,5]
[2,3,4,4,5,10,20]
make that into a set
[2,3,4,5,10,20]

[0,3,2,5,4,6,1,1]
[0,1,1,2,3,4,5,6]
set: [0,1,2,3,4,5,6]
"""