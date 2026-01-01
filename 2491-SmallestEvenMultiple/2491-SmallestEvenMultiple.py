# Last updated: 1/1/2026, 10:53:24 PM
class Solution(object):
    def smallestEvenMultiple(self, n):
        double = n * 2
        if n % 2 == 0:
            return n
        elif double % 2 == 0:
            return double
        else:
            return False