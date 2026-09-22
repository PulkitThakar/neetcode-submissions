class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [i for i in range(n + 1)]
        rank = [1 for i in range(n + 1)]

        def find(node):
            p = par[node]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p
        
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)

            if p1 == p2:
                return True
            
            else:
                if rank[p1] >= rank[p2]:
                    rank[p1] += rank[p2]
                    par[p2] = p1
                else:
                    rank[p2] += rank[p1]
                    par[p1] = p2
            
            return False
        
        for edge in edges:
            if union(edge[0], edge[1]):
                return edge
        
        return [0, 0]