class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # target / |(speed - position)|
        # e.g1 -> 5, 5 -> 1 group correct
        # e.g2(division) -> 5, 10, 10, 1 -> three groups correct

        n = len(position)
        stack = []

        pairs = [(pos, spd) for pos, spd in zip(position, speed)]
        pairs.sort(key=lambda x: x[0], reverse=True)

        for pos, spd in pairs:
            current = (target - pos) / spd

            stack.append(current)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)

"""
target = 12
position: [10,8,0,5,3] speed: [2,4,1,1,3]
[1, 3, 12, 3, inf]
"""