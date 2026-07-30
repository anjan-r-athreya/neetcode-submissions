class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        n = len(nums)
        nums_s = sorted(nums)

        for i in range(n):
            if i > 0 and nums_s[i] == nums_s[i-1]: continue

            ptr1 = i + 1
            ptr2 = n - 1
            target = 0 - nums_s[i]

            while ptr1 < ptr2:
                current = nums_s[ptr1] + nums_s[ptr2]

                if current == target:
                    output.append([ nums_s[ptr1], nums_s[ptr2], nums_s[i] ])
                    ptr1 += 1
                    ptr2 -= 1

                    while ptr1 < ptr2 and nums_s[ptr1] == nums_s[ptr1 - 1]:
                        ptr1 += 1
                    while ptr1 < ptr2 and nums_s[ptr2] == nums_s[ptr2 + 1]:
                        ptr2 -= 1
                else:
                    if current < target:
                        ptr1 += 1
                    elif current > target:
                        ptr2 -= 1
        
        return output

# 0 = nums[i] + nums[ptr1] + nums[ptr2]
# nums[ptr1] + nums[ptr2] = 0 - nums[i]