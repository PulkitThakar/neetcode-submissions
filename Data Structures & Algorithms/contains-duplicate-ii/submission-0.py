class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        z = set()
        i = 0
        for j in range(k):
            if j >= len(nums):
                break
            if nums[j] not in z:
                z.add(nums[j])
            else:
                return True
        for j in range(k, len(nums)):
            if nums[j] not in z:
                z.add(nums[j])
            else:
                return True
            z.remove(nums[j - k])
        return False
        