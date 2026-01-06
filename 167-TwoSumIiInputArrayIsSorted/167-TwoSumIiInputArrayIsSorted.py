# Last updated: 1/6/2026, 11:59:15 PM
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left <= right:
            sum = numbers[left] + numbers[right]

            if sum == target:
                return [left + 1, right + 1]

            elif sum < target:
                left += 1
            
            else:
                right -= 1