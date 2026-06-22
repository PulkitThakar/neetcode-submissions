class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        heap = []
        for i in intervals:
            heapq.heappush(heap, i)
        
        res = []
        toAppend = heapq.heappop(heap)
        while heap:
            temp = heapq.heappop(heap)
            if temp[0] <= toAppend[1]:
                toAppend[1] = max(toAppend[1], temp[1])
            else:
                res.append(toAppend)
                toAppend = temp
        res.append(toAppend)
        return res