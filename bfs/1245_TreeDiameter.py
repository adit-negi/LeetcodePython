class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        def find_last(node):
            visited = set()
            q = [node]
            while q:
                root = q.pop(0)
                visited.add(root)
                ans = root

                for i in g[root]:
                    if i not in visited:
                        visited.add(i)
                        q.append(i)
            return ans

        def bfs(q, lenght, visited):
            nonlocal ans
            ans = lenght
            temp = []
            if not q:
                return 0
            while q:
                node = q.pop()
                if node in visited:
                    continue
                visited.add(node)
                for i in g[node]:
                    if i not in visited:
                        temp.append(i)
            if temp == []:
                return 0
            bfs(temp, lenght+1, visited)

        last = find_last(0)
        ans = 0
        bfs([last], 0, set())

        return ans
