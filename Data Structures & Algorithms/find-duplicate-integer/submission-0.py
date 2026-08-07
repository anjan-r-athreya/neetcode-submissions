class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 1

        while fast < len(nums):
            if nums[slow] == nums[fast]:
                return nums[slow]

            fast = nums[nums[fast]]
            slow = nums[slow]
    