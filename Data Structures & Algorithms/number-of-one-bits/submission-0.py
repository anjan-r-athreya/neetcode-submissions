class Solution:
    def hammingWeight(self, n: int) -> int:
        # essentially want to break it down into its 2^x + 2^x-1...
        # number of terms = number of 1s
        count = 0
        target = n
        pwr = 1

        while target > 0:
            pwr = 1
            
            while pwr * 2 <= target:
                pwr *= 2
                
            count += 1
            target = target - pwr
        
        return count
