class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        for mask in range( 1 << n ):
            temp = []
            for j in range(n):
                if mask & ( 1 << j):
                    temp.append(nums[j])
            ans.append(temp)
        return ans
        