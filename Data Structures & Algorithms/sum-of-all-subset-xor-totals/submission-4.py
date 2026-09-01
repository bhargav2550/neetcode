class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        subset = []

        def dfs(i, subset):
            nonlocal res
            if i >= len(nums):
                xorr = 0
                for num in subset:
                    xorr ^= num
                res += xorr
                return
            
            subset.append(nums[i])
            dfs(i + 1, subset)
            subset.pop()
            dfs(i + 1, subset)
        dfs(0, [])
        return res
                