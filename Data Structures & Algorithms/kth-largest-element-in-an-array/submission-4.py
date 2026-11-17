class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for i in range(k):
            heapq.heappush(min_heap, nums[i])
        
        for i in range(k, len(nums)):
            heapq.heappush(min_heap, nums[i])
            heapq.heappop(min_heap)

        return min_heap[0]