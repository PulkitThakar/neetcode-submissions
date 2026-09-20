class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)

        if len_nums1 > len_nums2:
            return self.findMedianSortedArrays(nums2, nums1)
        
        total = len_nums1 + len_nums2
        l, r = 0, len_nums1 - 1

        while True:
            m1 = l + ((r - l)//2)
            m2 = ((total)//2) - m1 - 2

            l1 = nums1[m1] if m1 >= 0 else float("-inf")
            r1 = nums1[m1 + 1] if m1 + 1 < len_nums1 else float("inf")
            l2 = nums2[m2] if m2 >= 0 else float("-inf")
            r2 = nums2[m2 + 1] if m2 + 1 < len_nums2 else float("inf")

            if l1 <= r2 and l2 <= r1:
                if total % 2:
                    return min(r1, r2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2
            elif l1 > r2:
                r = m1 - 1
            else:
                l = m1 + 1
        
        return 0