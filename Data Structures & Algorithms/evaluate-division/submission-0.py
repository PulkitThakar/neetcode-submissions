class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i, e in enumerate(equations):
            adj[e[0]].append([e[1], values[i]])
            adj[e[1]].append([e[0], 1/values[i]])
        
        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1
            q = deque()
            q.append([src, 1])
            visit = set()
            visit.add(src)
            while q:
                curr, wei = q.popleft()
                if curr == target:
                    return wei
                for nei in adj[curr]:
                    if nei[0] not in visit:
                        visit.add(nei[0])
                        q.append([nei[0], wei*nei[1]])
            return -1
            
        
        return [bfs(q[0], q[1]) for q in queries]