# Last updated: 1/14/2026, 4:44:13 PM
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1 or n == 2:
            return True
        
        elif n > 1 and n % 2 != 0:
            return False
        
        while n != 2:
            n = n / 2
            if n == 2:
                return True
            elif n < 2:
                return False
            