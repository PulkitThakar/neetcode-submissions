class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i, eq in enumerate(equations):
            adj[eq[0]].append([eq[1], values[i]])
            adj[eq[1]].append([eq[0], 1/values[i]])
        
        def bfs(source, target):
            if source not in adj or target not in adj:
                return -1
            dq, visit = deque(), set()
            dq.append([source, 1])
            visit.add(source)
            while dq:
                node, w = dq.popleft()
                if node == target:
                    return w
                for nei, weight in adj[node]:
                    if nei not in visit:
                        dq.append([nei, w*weight])
                        visit.add(nei)
            return -1
            

        return [bfs(q[0], q[1]) for q in queries]