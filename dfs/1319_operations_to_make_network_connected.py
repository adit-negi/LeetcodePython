class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1
        g = defaultdict(list)
        for u, v in connections:
            g[u].append(v)
            g[v].append(u)

        def dfs(node, visited):
            visited.add(node)
            for i in g[node]:
                if i not in visited:
                    dfs(i, visited)

        cnt = 0
        visited = set()
        for i in range(n):
            if i not in visited:
                dfs(i, visited)
                cnt += 1
        return cnt-1
