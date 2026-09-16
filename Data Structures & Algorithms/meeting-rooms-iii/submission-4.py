class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        available = [i for i in range(n)]
        used = [] # (end_time, room_number)
        meetings.sort()
        count = [0]*n # count the number of meetings in each room
        
        for start, end in meetings:
            while used and start >= used[0][0]:
                _, room = heapq.heappop(used)
                heapq.heappush(available, room)
            
            # no rooms available
            if not available:
                end_time, room = heapq.heappop(used)
                heapq.heappush(available, room)
                end = end_time + end - start
            
            # a room is available
            room = heapq.heappop(available)
            heapq.heappush(used, (end, room))
            count[room] += 1

        return count.index(max(count))