class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hq = []

        for i in range(k):
            dist = points[i][0] * points[i][0] + points[i][1] * points[i][1]
            heapq.heappush(hq, (-dist, points[i][0], points[i][1]))

        for i in range(k, len(points)):
            dist = points[i][0] * points[i][0] + points[i][1] * points[i][1]
            if dist > hq[0][0]:
                heapq.heappush(hq, (-dist, points[i][0], points[i][1]))
                heapq.heappop(hq)
        
        res = [[i[1], i[2]] for i in hq]
        return res