class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        s = 0
        currsum = 0

        for num in nums:
            currsum += num
            if currsum - k in d:
                s += d[currsum - k]
            d[currsum] += 1
        return s
