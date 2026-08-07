class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = defaultdict(int)
        maxlen = 0 
        maxf = 0
        l,r = 0,0
        while r < len(s):
            d[s[r]] += 1
            maxf = max(maxf,d[s[r]])
            if (r-l+1) - maxf > k:
                d[s[l]] -= 1
                l += 1
            maxlen = max(maxlen,r-l+1)
            r += 1
        return maxlen



