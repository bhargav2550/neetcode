class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        arr = [0]*len(nums)
        for i in nums:
            if i > 0 and i <= len(nums):
                arr[i-1] = 1
        print(arr)
        for i in range(len(arr)):
            if arr[i] == 0:
                return i + 1
        return len(arr) + 1