# Last updated: 1/1/2026, 10:53:47 PM
class Solution(object):
    def fizzBuzz(self, n):
        numlist = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                numlist.append("FizzBuzz")
            elif i % 3 == 0:
                numlist.append("Fizz")
            elif i % 5 == 0:
                numlist.append("Buzz")
            else:
                numlist.append(str(i))
        return numlist
        