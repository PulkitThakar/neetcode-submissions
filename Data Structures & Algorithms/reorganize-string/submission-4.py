class Solution:
    def reorganizeString(self, s: str) -> str:
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
        
        choose_hq = []
        for c in d:
            heapq.heappush(choose_hq, [-d[c], c])

        wait_hq = []
        res = ""
        for i in range(len(s)):
            print(f"{choose_hq} {wait_hq}")
            while wait_hq and wait_hq[0][0] <= i:
                temp = heapq.heappop(wait_hq)
                heapq.heappush(choose_hq, [temp[1], temp[2]])
            if choose_hq:
                top = heapq.heappop(choose_hq)
                res += top[1]
                if top[0] < -1:
                    heapq.heappush(wait_hq, [i + 2, top[0] + 1, top[1]])
            else:
                return ""
        return res