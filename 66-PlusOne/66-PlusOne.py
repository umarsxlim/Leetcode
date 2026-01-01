# Last updated: 1/1/2026, 10:53:54 PM
class Solution(object):
    def plusOne(self, digits):
        num = 0
        rdigits = []

        for i in digits:
            num = num * 10 + i
        num += 1
        
        while num > 0:
            rdigits.append(num % 10)
            num = num // 10

        rdigits.reverse()
        return rdigits