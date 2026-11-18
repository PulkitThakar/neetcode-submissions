class Solution:

    def __init__(self, w: List[int]):
        self.running_sum = [0]
        for i in w:
            self.running_sum.append(self.running_sum[-1] + i)

    def pickIndex(self) -> int:
        target = random.random() * self.running_sum[-1]
        l, r = 0, len(self.running_sum) - 1
        res = -1
        while l <= r:
            m = l + (r-l)//2
            if self.running_sum[m] < target:
                res = m
                l = m + 1
            elif self.running_sum[m] > target:
                r = m - 1
            else:
                return m
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()