# Last updated: 1/19/2026, 10:42:59 PM
class Solution:
    def maximum69Number (self, num: int) -> int:
        numlist = []
        temp = 0

        while num > 0:
            temp = num % 10
            num = num // 10
            numlist.append(temp)

        numlist.reverse()

        for i in range(len(numlist)):
            if numlist[i] == 6:
                numlist[i] = 9
                break

        temp = 0
        
        for i in numlist:
            temp = temp * 10 + i
            
        return temp