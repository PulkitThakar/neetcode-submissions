class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = 0
        while l < r:
            min_side = heights[l]
            if heights[r] < heights[l]:
                min_side = heights[r]
            base = r - l
            area = min_side * base
            if max_area < area:
                max_area = area

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_area