# Last updated: 1/1/2026, 10:53:48 PM
class Solution(object):
    def reverseVowels(self, s):
        indexes = []
        char = list(s)
        word = ""

        for idx, val in enumerate(s):
            if val.lower() in "aeiou":
                indexes.append(idx)

        reverse = list(reversed(indexes))
        
        for i in range(len(indexes)):
            char[indexes[i]] = s[reverse[i]]

        return "".join(char)