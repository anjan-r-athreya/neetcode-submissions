class Solution:
    def tribonacci(self, n: int) -> int:
        t0 = 0
        t1 = 1
        t2 = 1

        fib = [t0, t1, t2]

        if n == 0: return t0
        elif n == 1: return t1
        elif n == 2: return t2

        for i in range(3, n + 1, 1):
            new = fib[i-1] + fib[i-2] + fib[i-3]
            fib.append(new)

        return fib[-1]