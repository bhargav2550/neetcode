class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        def dfs(i, arr):
            nonlocal res
            if i == len(nums):
                if sum(arr) == target:
                    res.add(tuple(arr.copy()))
                return
            if i < len(nums) and sum(arr) > target:
                return
            dfs(i, arr + [nums[i]])
            dfs(i + 1, arr)
            # dfs(i+1, arr + [nums[i]])
        dfs(0, [])
        res = [list(s) for s in res]
        return res