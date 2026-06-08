class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1

        while left <= right:
            mid = int((left + right) / 2)

            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            elif target == nums[mid]:
                return mid
        return -1
