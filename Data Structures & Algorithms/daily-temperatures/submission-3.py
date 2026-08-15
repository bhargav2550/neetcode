class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = []
        st = []
        n = len(temperatures)
        for i in range(n-1, -1, -1):
            while st and temperatures[i] >= temperatures[st[-1]]:
                st.pop()
            if not st:
                ans.append(0)
            else:
                ans.append(st[-1] - i)
            st.append(i)
        return ans[::-1]
            

