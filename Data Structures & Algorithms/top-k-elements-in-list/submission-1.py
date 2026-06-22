class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for i in nums:
            freq[i] += 1
        q = []

        for i in freq:
            heapq.heappush(q, [freq[i], i])
            if len(q) > k:
                heapq.heappop(q)

        res = []
        while(q):
            res.append(heapq.heappop(q)[1])
        
        return res