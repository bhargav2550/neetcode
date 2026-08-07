class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        d = { "}" : "{", "]": "[", ")": "("}
        for i in s:
            if i in d:
                if st and st[-1] == d[i]:
                    st.pop()
                else:
                    st.append(i)
            else:
                st.append(i)
        return True if not st else False
