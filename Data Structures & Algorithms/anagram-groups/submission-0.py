class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            s = tuple(sorted(i))
            if s in d:
                d[s].append(i)
            else:
                d[s] = [i]
        ans = []
        for i in d:
            ans.append(d[i])
        return ans