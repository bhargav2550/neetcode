class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        ans = []
        def f(i, subset, cnt):
            nonlocal ans
            if cnt == k:
                ans.append(subset.copy())
                return

            if i > n:
                return
            
            subset.append(i)
            f(i + 1, subset, cnt + 1)
            subset.pop()
            f(i + 1, subset, cnt)
        f(1, [], 0)
        print(ans)
        return ans