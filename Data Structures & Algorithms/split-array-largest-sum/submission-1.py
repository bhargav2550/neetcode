class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def noOfArrays(su):
            tot = 0
            ans = 1
            for i in nums:
                tot += i
                if tot > su:
                    tot = i
                    ans += 1
            return ans <= k

        low = max(nums)
        high = sum(nums)
        res = high
        while low <= high:
            mid = (low + high) // 2
            if noOfArrays(mid):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res
