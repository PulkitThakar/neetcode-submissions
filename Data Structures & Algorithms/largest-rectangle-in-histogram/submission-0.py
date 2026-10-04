class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        s = []
        for i in range(len(heights)):
            idx = i
            while s and s[-1][0] > heights[i]:
                h, idx = s.pop()
                temp = (i - idx)*h
                if temp > res:
                    res = temp
            
            s.append([heights[i], idx])
        
        i = len(heights)
        while s:
            h, idx = s.pop()
            temp = (i - idx)*h
            if temp > res:
                res = temp
        
        return res