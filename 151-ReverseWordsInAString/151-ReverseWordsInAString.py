# Last updated: 1/1/2026, 10:53:53 PM
class Solution(object):
    def reverseWords(self, s):
        words = s.split()
        reversed_words = words[::-1]
        result = " ".join(reversed_words)

        return result