class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {}

        # [ 4, 3, 2, 1]


        for idx, num in enumerate(nums):
            comp[target - num] = idx

        for idx2, num in enumerate(nums):
            if num in comp and comp[num] != idx2:
                return list(reversed([comp[num],idx2]))
        return []
        
