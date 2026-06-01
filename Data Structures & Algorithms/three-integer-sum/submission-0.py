class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # two pointers approach
        n = len(nums)
        sort = nums.sort()
        triplets = []
        
        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i-1]:
                continue
            
            ptr1, ptr2 = i + 1, n - 1

            while ptr1 < ptr2:
                current = a + nums[ptr1] + nums[ptr2]

                if current > 0: 
                    ptr2 = ptr2 - 1
                elif current < 0:
                    ptr1 = ptr1 + 1
                else:
                    triplets.append([a, nums[ptr1], nums[ptr2]])
                    ptr1 = ptr1 + 1
                    ptr2 = ptr2 - 1
                    while nums[ptr1] == nums[ptr1 - 1] and ptr1 < ptr2:
                        ptr1 = ptr1 + 1
            
        return triplets