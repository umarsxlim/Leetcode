# Last updated: 1/11/2026, 12:37:19 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for i in s:
            if i.isalnum():
                clean += i
        
        clean = clean.lower()
        
        if clean == clean[::-1]:
            return True
        
        else:
            return False