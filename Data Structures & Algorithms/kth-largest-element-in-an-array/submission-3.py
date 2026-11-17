class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []
        for i in range(k):
            heapq.heappush(max_heap, nums[i])
        
        for i in range(k, len(nums)):
            heapq.heappush(max_heap, nums[i])
            heapq.heappop(max_heap)

        return max_heap[0]