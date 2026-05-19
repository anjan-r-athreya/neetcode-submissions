class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        bucket sort approach:
        keys = frequencies
        values = list of all elements with frequency of key
        """
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i],0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res