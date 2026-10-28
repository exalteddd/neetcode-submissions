class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        seen = set()
        existing = set(nums)
        nums = list(set(nums))

        if len(nums) == 0:
            return 0

        for num in nums:
            if num not in seen:
                right, left = num, num            
                while right in existing:
                    right += 1
                    seen.add(right)
                while left in existing:
                    left -= 1
                    seen.add(left)
                max_length = max(max_length, right - left)
        return(max_length - 1)
        