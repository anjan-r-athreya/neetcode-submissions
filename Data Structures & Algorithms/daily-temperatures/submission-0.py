class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n

        for i in range(n):
            currDays = 0

            for j in range(i, n):
                if temperatures[j] > temperatures[i]:
                    result[i] = currDays
                    break
                else:
                    currDays += 1
            
        return result
