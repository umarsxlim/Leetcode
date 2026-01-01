# Last updated: 1/1/2026, 10:53:42 PM
class Solution(object):
    def fib(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1

        first = 0
        second = 1

        for i in range(2, n + 1):
            next_num = first + second
            first = second
            second = next_num

        return second