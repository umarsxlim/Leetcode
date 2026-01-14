# Last updated: 1/14/2026, 4:43:53 PM
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = 0
        temp = 0
        left = 0

        wordlist = list(word)

        for i in wordlist:
            if i == ch:
                break
            else:
                index += 1

        if index >= len(word):
            return word

        while left < index:
            temp = wordlist[left] 
            wordlist[left] = wordlist[index]
            wordlist[index] = temp

            left += 1
            index -= 1
        
        return "".join(wordlist)