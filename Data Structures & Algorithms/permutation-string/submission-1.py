class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = defaultdict(int)
        for i in s1:
            count1[i] += 1
        
        n = len(count1)

        for i in range(len(s2)):
            count2 = defaultdict(int)
            curr = 0
            for j in range(i, len(s2)):
                count2[s2[j]] += 1
                if count1[s2[j]] < count2[s2[j]]:
                    break
                if count1[s2[j]] == count2[s2[j]]:
                    curr += 1
                if curr == n:
                    return True
        return False




            