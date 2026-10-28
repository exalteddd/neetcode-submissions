class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while right > 0 and left < right:
            cand = numbers[left] + numbers[right]
            if cand == target:
                return [left + 1, right + 1]
            if cand > target:
                right -= 1
            elif cand < target:
                left += 1
        return []
            

        