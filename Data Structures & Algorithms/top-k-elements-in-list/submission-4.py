class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)

        n = len(nums)

        for i in range(n):
            hashmap[nums[i]] += 1
        
        sort = sorted(hashmap.items(), key=lambda x:x[1], reverse=True )
        return [item[0] for item in sort[:k]]