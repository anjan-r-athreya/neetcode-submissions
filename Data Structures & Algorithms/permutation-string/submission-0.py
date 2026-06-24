class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        s1 hashtable of character counts
        """
        n1 = len(s1)
        n2 = len(s2)
        hash1 = {}
        hash2 = {}

        if n1 > n2: return False

        # initialize s1's hashtable
        for i in range(n1):
            hash1[s1[i]] = hash1.get(s1[i], 0) + 1
            hash2[s2[i]] = hash2.get(s2[i], 0) + 1
        
        ptr1 = 0
        ptr2 = n1 - 1

        while ptr2 < n2:
            if hash1 == hash2:
                return True
            
            hash2[s2[ptr1]] = hash2.get(s2[ptr1], 0) - 1
            if hash2[s2[ptr1]] == 0:
                hash2.pop(s2[ptr1])

            ptr1 += 1
            ptr2 += 1

            if ptr2 < n2:
                hash2[s2[ptr2]] = hash2.get(s2[ptr2], 0) + 1
        
        return False
