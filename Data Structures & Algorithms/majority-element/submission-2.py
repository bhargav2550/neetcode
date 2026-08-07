class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)

        cnt = 0
        ele = 0

        for i in nums:
            if cnt == 0:
                ele = i
                cnt = 1
            elif i == ele:
                cnt += 1
            else:
                cnt -= 1
        
        if nums.count(ele) > n // 2:
            return ele

        return -1