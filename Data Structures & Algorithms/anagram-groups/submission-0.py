class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        n = len(strs)

        for s in range(n):
            counts = [0] * 26
            wordlen = len(strs[s])

            for c in range(wordlen):
                counts[ord(strs[s][c]) - ord('a')] += 1
            
            hashmap[tuple(counts)].append(strs[s])
        
        return list(hashmap.values())