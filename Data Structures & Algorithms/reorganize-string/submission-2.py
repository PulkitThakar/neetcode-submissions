class Solution:
    def reorganizeString(self, s: str) -> str:
        count = defaultdict(int)
        for i in s:
            count[i] += 1
            if count[i] > math.ceil(len(s)/2):
                return ""
        
        heap = []
        for i in count:
            heapq.heappush(heap, [-count[i], i])

        support_heap = []

        res = ""

        i = 0;
        while(heap or support_heap):
            while(support_heap and support_heap[0][0] == i):
                temp = heapq.heappop(support_heap)
                heapq.heappush(heap, [temp[1], temp[2]])
            if not heap:
                break

            temp = heapq.heappop(heap)
            res += temp[1]
            
            if temp[0] < -1:
                heapq.heappush(support_heap, [i + 2, temp[0] + 1, temp[1]])
            
            i += 1
        
        if support_heap:
            return ""
        
        return res