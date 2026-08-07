class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)

        for i in nums:
            d[i] += 1
        d = sorted(d.items(), key=lambda item: -item[1])
        ans = []
        for i in range(k):
            ans.append(d[i][0])
        print(ans)
        return ans
        

