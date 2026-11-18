class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        res = [0]*len(temperatures)
        for idx, temp in enumerate(temperatures):
            while stk and stk[-1][0] < temp:
                curr = stk.pop()
                res[curr[1]] = idx - curr[1]
            stk.append((temp, idx))
        return res