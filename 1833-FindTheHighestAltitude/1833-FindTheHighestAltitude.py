# Last updated: 1/1/2026, 10:53:32 PM
class Solution(object):
    def largestAltitude(self, gain):
        alt = [0]
        for i in range(len(gain)):
            alt.append(alt[i] + gain[i])

        return max(alt)