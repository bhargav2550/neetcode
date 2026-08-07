class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0
        for i in s:
            if i-1 not in s:
                curr = i
                cnt = 0
                while curr in s:
                    cnt += 1
                    curr += 1
                ans = max(ans,cnt)
        return ans