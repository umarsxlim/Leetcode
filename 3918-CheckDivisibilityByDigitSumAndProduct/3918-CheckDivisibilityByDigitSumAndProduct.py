# Last updated: 1/1/2026, 10:53:15 PM
class Solution(object):
    def checkDivisibility(self, n):
        # split
        og_n = n
        nums = []
        while n > 0:
            nums.append(n % 10)
            n = n // 10
    
        # sum
        sum = 0
        for i in nums:
            sum += i

        # product
        product = 1
        for i in nums:
            product *= i
        
        # check
        if og_n % (sum + product) == 0:
            return True
        else:
            return False