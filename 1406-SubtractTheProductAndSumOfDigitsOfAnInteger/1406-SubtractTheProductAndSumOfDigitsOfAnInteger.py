# Last updated: 1/1/2026, 10:53:39 PM
class Solution(object):
    def subtractProductAndSum(self, n):
        sum = 0
        product = 1
        while n != 0:
            newnum = n % 10
            n = n // 10
            sum += newnum
            product *= newnum
        return product - sum