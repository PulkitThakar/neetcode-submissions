class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        
        left_max = 0
        right_max = 0
        l = 0
        r = len(height) - 1
        while l <= r:
            if left_max <= right_max:
                res += max(0, left_max - height[l])
                left_max = max(left_max, height[l])
                l += 1
            else:
                res += max(0, right_max - height[r])
                right_max = max(right_max, height[r])
                r -= 1
        
        return res