class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(numCourses)}
        for p in prerequisites:
            adj[p[0]].append(p[1])
        
        visit = {}
        res = []

        def dfs(course):
            if course in visit:
                return not visit[course]
            
            visit[course] = True
            for nei in adj[course]:
                if not dfs(nei):
                    return False
            res.append(course)
            visit[course] = False
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return res