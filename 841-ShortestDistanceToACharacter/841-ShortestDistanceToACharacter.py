# Last updated: 1/11/2026, 12:37:03 PM
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        res = []
        index = 0 
        while index < len(s):
            if s[index] == c:
                res.append(0)
            else:
                lefttemp = len(s)
                righttemp = len(s)
                
                # Check behind
                for i in range(index - 1, -1, -1):
                    if s[i] == c:
                        lefttemp = index - i
                        break
                
                # Check ahead
                for i in range(index + 1, len(s)):
                    if s[i] == c:
                        righttemp = i - index
                        break
                
                res.append(min(lefttemp, righttemp))
            index += 1
        return res