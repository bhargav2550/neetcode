class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        aux = [1] * (len(nums))
        num = 1
        zero_count = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                num = num * nums[i]
            else :
                zero_count += 1

        if zero_count >= 2 : 
            return [0] * len(nums)


        for i in range(len(nums)):
            if zero_count == 1:
                if nums[i] == 0:
                    aux[i] = num
                else:
                    aux[i] = 0
            else:
                aux[i] = num // nums[i] # to return integers(48) not 48.0
        return aux
            