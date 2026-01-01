# Last updated: 1/1/2026, 10:53:37 PM
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maxcandy = max(candies)
        greatest = []

        for i in candies:    
            if i + extraCandies >= maxcandy:
                greatest.append(True)
            else:
                greatest.append(False)
        
        return greatest