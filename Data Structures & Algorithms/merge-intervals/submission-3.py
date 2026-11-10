class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        res = []
        curr = intervals[0]
        for idx in range(1, len(intervals)):
            start = intervals[idx][0]
            end = intervals[idx][1]
            if start <= curr[1]:
                if end > curr[1]:
                    curr[1] = end
            else:
                res.append(curr)
                curr = [start, end]
        res.append(curr)
        return res