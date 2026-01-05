# Last updated: 1/5/2026, 4:31:35 PM
class Solution(object):
    def romanToInt(self, s):
        roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50,'C': 100, 'D': 500, 'M': 1000}

        integer = 0

        for i in range(len(s)):
            if i + 1 < len(s) and roman_to_int[s[i]] < roman_to_int[s[i+1]]:
                integer -= roman_to_int[s[i]]
            else:
                integer += roman_to_int[s[i]]
        
        return integer