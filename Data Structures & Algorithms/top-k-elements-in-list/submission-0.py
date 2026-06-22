class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        n = len(nums)

        for i in range(n):
            if nums[i] not in counts:
                counts[nums[i]] = 1
            else:
                counts[nums[i]] += 1
        
        sorted_counts = dict(sorted(counts.items()))
        return list(counts.keys())[len(counts) - k:]