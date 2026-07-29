class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)

        hashmap = defaultdict(list)

        for i in range(n):
            count = [0] * 26

            for j in range(len(strs[i])):
                count[ord(strs[i][j]) - ord('a')] += 1
            
            hashmap[tuple(count)].append(strs[i])
        
        return list(hashmap.values())
