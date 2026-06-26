class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(set)
        for i, j in edges:
            adj[i].add(j)
            adj[j].add(i)
        
        visit = set()

        def dfs(node):
            if node in visit:
                return
            
            visit.add(node)
            for nei in adj[node]:
                if nei not in visit:
                    dfs(nei)
        
        groups = 0
        for i in range(n):
            if i not in visit:
                dfs(i)
                print(visit)
                groups += 1
        
        return groups