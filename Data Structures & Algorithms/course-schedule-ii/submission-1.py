class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:set() for i in range(numCourses)}
        for course, prereq in prerequisites:
            adj[course].add(prereq)
        
        course_ordering = []
        visit = set()
        loop = set()
        def dfs(course):
            if course in loop:
                return False
            if course in visit:
                return True
            
            visit.add(course)
            loop.add(course)
            for prereq in adj[course]:
                if not dfs(prereq):
                    return False
            loop.remove(course)
            course_ordering.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        return course_ordering