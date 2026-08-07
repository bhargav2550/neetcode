class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(nlogk) and SC - O(n + k)
        d = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]

        for i in nums:
            d[i] += 1
        
        heap = []
        for num in d.keys():
            heapq.heappush(heap,(d[num],num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

        

