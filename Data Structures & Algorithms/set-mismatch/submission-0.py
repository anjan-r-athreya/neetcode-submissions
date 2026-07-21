class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        hashset = {}
        n = len(nums)
        final = []
        unique = sorted(set(nums))

        for i in range(n):
            if nums[i] not in hashset:
                hashset[nums[i]] = 1
            else:
                final.append(nums[i])
                break
        
        for i in range(1, n + 1):
            if i > len(unique) or i != unique[i-1]:
                final.append(i)
                break
        
        return final