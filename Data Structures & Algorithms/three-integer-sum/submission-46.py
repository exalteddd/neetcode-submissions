class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        triplets = []
       
        for idx,num in enumerate(nums):
            left = 0
            right = len(nums) - 1
            if [num, nums[left],nums[right]] == [0,0,0]:
                return [[num,nums[left],nums[right]]]
            while left < right:
                if num + nums[left] + nums[right] > 0:
                    right -= 1
                if num + nums[left] + nums[right] < 0:
                    left += 1
                if num + nums[left] + nums[right] == 0:
                    if left != right and right != idx and left != idx:
                        listy = sorted([num,nums[left],nums[right]])
                        if listy not in triplets:
                            triplets.append(listy)
                    left += 1
                    right -= 1
                    
        return triplets
        #-2,-1,0,1,2,3
        




        