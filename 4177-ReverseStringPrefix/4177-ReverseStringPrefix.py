# Last updated: 1/14/2026, 4:43:40 PM
class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        left = 0
        right = k - 1
        slist = list(s)
        
        while left < right:
            temp = slist[left]
            slist[left] = slist[right]
            slist[right] = temp

            left += 1
            right -= 1
        
        return "".join(slist)