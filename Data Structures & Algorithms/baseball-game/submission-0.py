class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []
        s = 0
        for i in operations:
            if i == "+":
                if st and len(st) > 1:
                    st.append(int(st[-1]) + int(st[-2]))
            elif i == "C":
                if st:
                    st.pop()
            elif i == "D":
                if st:
                    st.append(int(st[-1])*2)
            else:
                st.append(int(i))
        print(st)
        return sum(st)