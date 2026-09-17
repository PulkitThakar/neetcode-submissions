class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        res = []
        n = len(nums)
        i = 0
        
        while i < n - 2 and nums[i] <= 0:
            j = i + 1
            k = n - 1
            target = -nums[i]
            while j < k:
                if target < nums[j] + nums[k]:
                    k -= 1
                elif target > nums[j] + nums[k]:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    temp = j + 1
                    while temp <= k and nums[temp] == nums[temp - 1]:
                        temp += 1
                    j = temp
            
            temp = i + 1
            while temp < n - 2 and nums[temp] == nums[temp - 1]:
                temp += 1
            i = temp
        
        return res