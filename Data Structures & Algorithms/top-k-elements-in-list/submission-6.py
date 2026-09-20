class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        n = len(nums)

        for num in nums:
            hashmap[num] += 1
        
        sort = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
        
        final = []

        for i, key in enumerate(sort):
            if i >= k: break
            final.append(key[0])
        return final
