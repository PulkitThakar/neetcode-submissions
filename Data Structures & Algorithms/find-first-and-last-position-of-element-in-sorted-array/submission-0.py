class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binary_search(target):
            l, r = 0, len(nums)
            while l < r:
                m = l + ((r-l)//2)
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m
            start = l
            
            return start
        
        left = binary_search(target)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]

        right = binary_search(target + 1) - 1
        return [left, right]
        