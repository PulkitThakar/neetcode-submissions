class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {i:[] for i in range(n)}
        for frm, to, price in flights:
            adj[frm].append([to, price])
        
        cost = {}
        min_heap = [(0, src, k+1)]
        while min_heap:
            spent, curr, steps = heapq.heappop(min_heap)
            if curr == dst:
                return spent
            if (curr, steps) in cost and cost[(curr, steps)] < spent:
                continue
            cost[(curr, steps)] = spent
            if steps > 0:
                for nei, price in adj[curr]:
                    heapq.heappush(min_heap, (spent + price, nei, steps - 1))
        return -1