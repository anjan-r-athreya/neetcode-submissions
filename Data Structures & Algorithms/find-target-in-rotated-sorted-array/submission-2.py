class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1

        while l <= r:
            mid = (l + r) // 2

            # if nums[mid] < nums[left] or nums[mid] > nums[right]
            if nums[mid] == target: return mid
            elif nums[l] <= nums[mid]:
                if target >= nums[l] and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[r] > nums[mid]:
                if target <= nums[r] and target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1

"""
find pivot
perform regular b-search, condition for partition changes
find where either:
    - mid < left
    - mid > right

[3,4,5,6,7,1,2]
if target in set[left->mid], partition left: target > left, target < mid
if target in set[mid->right], partition right: target > mid, target < right
[5,6,7,1,2,3,4]
"""