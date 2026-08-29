class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree = [set() for _ in range(n+1)]
        outdegree = [set() for _ in range(n+1)]
        for u,v in trust:
            indegree[v].add(u)
            outdegree[u].add(v)
        for i in range(1, n + 1):
            if len(indegree[v]) == n - 1 and len(outdegree[v]) == 0:
                return v
        return -1