# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n

        while True:
            current = (left + right) // 2
            res = guess(current)

            if res == 0:
                return current
            elif res == -1:
                right = current - 1
            elif res == 1:
                left = current + 1