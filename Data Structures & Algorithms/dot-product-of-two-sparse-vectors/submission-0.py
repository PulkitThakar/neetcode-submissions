class SparseVector:
    def __init__(self, nums: List[int]):
        self.m = {i: v for i, v in enumerate(nums)}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        a, b = self.m, vec.m
        if len(b) < len(a):
            a, b = b, a
        return sum(v*b[i] for i, v in a.items() if i in b)

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
