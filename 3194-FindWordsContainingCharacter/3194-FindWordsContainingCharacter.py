# Last updated: 1/1/2026, 10:53:19 PM
class Solution(object):
    def findWordsContaining(self, words, x):
        xword = []
        for i, word in enumerate(words):
            if x in word:
                xword.append(i)
        return xword
                