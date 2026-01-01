# Last updated: 1/1/2026, 10:53:20 PM
class Solution(object):
    def differenceOfSums(self, n, m):
        num1 = 0
        num2 = 0
        for i in range(0, n+1):
            if i % m != 0:
                num1 = num1 + i

        for i in range(0, n+1):
            if i % m == 0:
                num2 = num2 + i

        return num1 - num2          
        