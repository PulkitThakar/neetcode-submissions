class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:set() for i in range(numCourses)}
        for p in prerequisites:
            adj[p[0]].add(p[1])
        visit = set()

        def dfs(course):
            if course in visit:
                return False
            if len(adj[course]) == 0:
                return True
            visit.add(course)
            for nei in adj[course]:
                if not dfs(nei):
                    return False
            adj[course] = set()
            visit.remove(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True