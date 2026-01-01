# Last updated: 1/1/2026, 10:53:23 PM
class Solution(object):
    def convertTemperature(self, celsius):
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.80 + 32.00
        ans = [kelvin, fahrenheit]
        return ans
        