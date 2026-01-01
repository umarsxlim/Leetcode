# Last updated: 1/1/2026, 10:53:55 PM
class Solution(object):
    def isPalindrome(self, x):
        if x == 0:
            return True
        
        elif x < 0:
            return False

        elif x % 10 == 0:
            return False

        num = x
        rev = 0 
        while num != 0:
            rev = rev * 10 + num % 10
            num = num // 10

        if rev == x:
            return True
        else:
            return False