class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        res = [0 for _ in range(n)]
        rooms = [i for i in range(n)]
        heapq.heapify(meetings)

        end_heap = []

        time = meetings[0][0]
        while meetings:
            while end_heap and end_heap[0][0] == time:
                freeing_room = end_heap[0][1]
                heapq.heappush(rooms, freeing_room)
                heapq.heappop(end_heap)
            
            if time >= meetings[0][0]:
                start, end = heapq.heappop(meetings)
                meeting_length = end - start

                room_assigned = heapq.heappop(rooms)
                res[room_assigned] += 1
                
                heapq.heappush(end_heap, [time + meeting_length, room_assigned])
            
            if not rooms:
                time = end_heap[0][0]
            else:
                if meetings and time < meetings[0][0]:
                    time = meetings[0][0]
                if end_heap and end_heap[0][0] < time:
                    time = end_heap[0][0]

        max_scheduled = 0
        res_room = -1
        for i in range(n):
            if res[i] > max_scheduled:
                res_room = i
                max_scheduled = res[i]
        return res_room