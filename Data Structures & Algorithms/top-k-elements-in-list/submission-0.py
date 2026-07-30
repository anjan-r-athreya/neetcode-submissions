class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        n = len(nums)

        for num in nums:
            hashmap[num] += 1
        
        sort = list(sorted(hashmap.items(), key=lambda x: x[1], reverse=True))
        return [item[0] for item in sort[:k]]