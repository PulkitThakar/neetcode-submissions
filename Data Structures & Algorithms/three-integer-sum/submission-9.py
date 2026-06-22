class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0
        n = len(nums)
        while(i < n - 2 and nums[i] <= 0):
            j, k = i + 1, n - 1
            while j < k:
                target = (-nums[i])
                temp = nums[j] + nums[k]
                if temp == target:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while(j < k and nums[j] == nums[j-1]):
                        j += 1
                elif temp < target:
                    j += 1
                else:
                    k -= 1

            i += 1
            while(i < n and nums[i] == nums[i-1]):
                i += 1
        
        return res