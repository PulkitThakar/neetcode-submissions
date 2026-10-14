class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        loop = set()
        d = {i:[] for i in range(numCourses)}
        for prereq in prerequisites:
            d[prereq[0]].append(prereq[1])
        
        def dfs(node):
            if not d[node]:
                return True
            if node in loop:
                return False
            
            loop.add(node)
            for nei in d[node]:
                if not dfs(nei):
                    return False
            loop.remove(node)
            d[node].clear()
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
