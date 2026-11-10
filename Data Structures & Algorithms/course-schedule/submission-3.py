class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:set() for i in range(numCourses)}
        for course, prereq in prerequisites:
            adj[course].add(prereq)
        
        loop = set()
        def dfs(course):
            if not adj[course]:
                return True
            
            if course in loop:
                return False
            
            loop.add(course)
            for prereq in adj[course]:
                if not dfs(prereq):
                    return False
            loop.remove(course)
            adj[course].clear()
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
            