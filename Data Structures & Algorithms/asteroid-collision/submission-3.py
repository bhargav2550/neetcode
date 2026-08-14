import numpy as np
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for i in asteroids:
            alive = True
            while st and st[-1] > 0 and i < 0:
                if st[-1] < -i:
                    st.pop()
                elif st[-1] == -i:
                    st.pop()
                    alive = False
                    break
                else:
                    alive = False
                    break
            if alive:
                st.append(i)
        return st
            