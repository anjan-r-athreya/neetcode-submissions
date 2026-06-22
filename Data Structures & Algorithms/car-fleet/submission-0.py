class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # target / |(speed - position)|
        # e.g1 -> 5, 5 -> 1 group correct
        # e.g2(division) -> 5, 10, 10, 1 -> three groups correct


        n = len(position)
        hashmap = {}

        for i in range(n):
            current = int(target / abs(speed[i] - position[i]))

            if current not in hashmap:
                hashmap[current] = 1
            else:
                hashmap[current] += 1
        
        return len(hashmap)