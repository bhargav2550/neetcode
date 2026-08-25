class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict
        if t == "":
            return ""

        countT = {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        res = [-1,-1]
        minLen = 1e9
        l, r, n = 0, 0, len(s)
        have, need = 0, len(countT)
        countS = defaultdict(int)
        while r < n:
            countS[s[r]] += 1
            if s[r] in countT and countT[s[r]] == countS[s[r]]:
                have += 1
            
            while have == need:
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    res = [l, r]
                
                countS[s[l]] -= 1
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
            r += 1
        l, r = res
        return s[l : r + 1] if minLen != 1e9 else "" 

            
            

