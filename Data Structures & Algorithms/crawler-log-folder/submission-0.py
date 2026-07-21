class Solution:
    def minOperations(self, logs: List[str]) -> int:
        distance = 0

        n = len(logs)
        
        for i in range(n):
            current = logs[i]
            if current == "../":
                if distance > 0:
                    distance = distance - 1
            elif current == "./":
                continue
            else:
                distance = distance + 1
        
        return distance