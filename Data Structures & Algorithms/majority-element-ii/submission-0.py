class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)
        ans = []
        for i in nums:
            d[i] += 1

        for key,val in d.items():
            if val > len(nums) // 3:
                ans.append(key)
        return ans