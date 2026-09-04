class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def backtrack(ind, subset, pick):
            if ind == len(nums):
                res.add(tuple(subset[::]))
                return
            
            for j in range(len(nums)):
                if not pick[j]:
                    pick[j] = True
                    subset.append(nums[j])
                    backtrack(ind + 1, subset, pick)
                    subset.pop()
                    pick[j] = False
        backtrack(0, [], [False]*len(nums))
        return [list(i) for i in res]