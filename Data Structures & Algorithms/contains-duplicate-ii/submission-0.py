class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        from collections import defaultdict
        d = defaultdict(int)
        for ind, val in enumerate(nums):
            if val in d and abs(d[val] - ind) <= k:
                return True
            else:
                d[val] = ind
        return False