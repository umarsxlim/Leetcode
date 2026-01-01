# Last updated: 1/1/2026, 10:53:50 PM
class Solution(object):
    def addDigits(self, num):
        numsplit = []

        while num > 9:
            while num != 0:
                numsplit.append(num % 10)
                num = num // 10

            for i in numsplit:
                num += i
            numsplit = []
        return num