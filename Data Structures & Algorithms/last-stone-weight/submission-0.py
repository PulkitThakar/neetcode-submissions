class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q = []
        for i in stones:
            heapq.heappush(q, -i)
        
        while len(q) > 1:
            a, b = -heapq.heappop(q), -heapq.heappop(q)
            if a != b:
                heapq.heappush(q, -abs(a - b))
            print(q)
        
        if len(q) == 1:
            return -heapq.heappop(q)
        return 0