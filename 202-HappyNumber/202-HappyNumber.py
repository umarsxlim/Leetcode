# Last updated: 1/14/2026, 4:44:15 PM
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False
            
            seen.add(n)
            digits = []
            product = 0

            while n != 0:
                digits.append(n % 10)
                n = n // 10
            
            for i in digits:
                product = product + i * i
            
            n = product
           
            if product == 1:
                return True
        return True