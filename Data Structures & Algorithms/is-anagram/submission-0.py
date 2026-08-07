class Solution:
    def isAnagram(self, str1: str, str2: str) -> bool:
        if len(str1) != len(str2):
            return False
        
        freq = [0] * 26
        for i in range(len(str1)):
            freq[ord(str1[i])-ord('a')] += 1
            freq[ord(str2[i])-ord('a')] -= 1
        
        for val in freq:
            if val != 0:
                return False
        return True
