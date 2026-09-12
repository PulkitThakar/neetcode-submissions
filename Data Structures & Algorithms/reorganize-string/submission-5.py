class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        hq = [[-counts, c] for c, counts in count.items()]
        heapq.heapify(hq)

        prev = None
        res = ""
        while hq or prev:
            if prev and not hq:
                return ""
            top = heapq.heappop(hq)
            res += top[1]

            if prev:
                heapq.heappush(hq, prev)
                prev = None
            
            if top[0] < -1:
                prev = [top[0] + 1, top[1]]
        
        return res