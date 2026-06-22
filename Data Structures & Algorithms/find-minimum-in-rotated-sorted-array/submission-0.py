class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        must find the split point and then binary search is possible
        binary search until a valid left->mid->right shows up
        """

        n = len(nums)
        l = 0
        r = n - 1
        currentMin = 1002

        while l < r:
            mid = (l + r) // 2

            if nums[l] >= nums[mid]:
                r = mid
            elif nums[r] < nums[mid]:
                l = mid

        return nums[r + 1]