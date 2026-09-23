class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        enter_dq = deque()
        exit_dq = deque()
        
        res = [-1 for i in range(len(arrival))]

        i = 0
        time = 0
        prev = 1 # 1 for exit and 0 for enter
        while i < len(arrival) or enter_dq or exit_dq:
            while i < len(arrival) and arrival[i] == time:
                if state[i] == 0:
                    enter_dq.append(i)
                if state[i] == 1:
                    exit_dq.append(i)
                i += 1
            
            if enter_dq or exit_dq:
                # person = len(arrival)
                if enter_dq and exit_dq:
                    if prev:
                        person = exit_dq.popleft()
                    else:
                        person = enter_dq.popleft()
                else:
                    if enter_dq:
                        person = enter_dq.popleft()
                        prev = 0
                    if exit_dq:
                        person = exit_dq.popleft()
                        prev = 1
                res[person] = time
            else:
                prev = 1
            time += 1
        
        return res