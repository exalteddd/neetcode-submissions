class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_counter = 0
        for num in nums:
            if num == 0:
                zero_counter += 1
            else: product *= num
        result = []
        
        for num in nums:
            if num != 0:
                if zero_counter == 0:
                    result.append(int(product/num))
                else:
                    result.append(0)
            elif zero_counter <= 1:
                result.append(product)
            else:
                result.append(0)
        return result

        