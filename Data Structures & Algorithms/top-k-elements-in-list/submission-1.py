class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]

        for i in nums:
            d[i] += 1
        for key,count in d.items():
            freq[count].append(key)
        
        res = []
        for i in range(len(freq) - 1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

        

