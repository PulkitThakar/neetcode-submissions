class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(numCourses)}
        indeg = [0] * numCourses
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indeg[course] += 1
        
        q = deque(c for c in range(numCourses) if indeg[c] == 0)
        course_order = []

        while q:
            c = q.popleft()
            course_order.append(c)
            for nei in adj[c]:
                indeg[nei] -= 1
                if not indeg[nei]:
                    q.append(nei)

        return course_order if len(course_order) == numCourses else []