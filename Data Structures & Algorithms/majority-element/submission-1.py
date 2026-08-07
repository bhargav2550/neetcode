class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        d = defaultdict(int)

        for i in nums:
            d[i] += 1
        for key,val in d.items():
            if val > n // 2:
                return key
        return -1