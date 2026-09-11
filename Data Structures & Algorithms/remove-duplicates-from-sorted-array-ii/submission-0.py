class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        k = 2 # maximum repeatability
        l, r = 0, 0

        while r < n:
            count = 1
            while r + 1 < n and nums[r] == nums[r+1]:
                r += 1
                count += 1
            
            count = min(k, count)

            while count > 0:
                nums[l] = nums[r]
                count -= 1
                l += 1
            r += 1
        
        return l