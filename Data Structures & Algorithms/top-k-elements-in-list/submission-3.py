class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        n = len(nums)

        for i in range(n):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
            elif nums[i] in hashmap:
                hashmap[nums[i]] += 1
        
        sorted_items = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
        
        result = []

        for num, freq in sorted_items[:k]:
            result.append(num)

        return result