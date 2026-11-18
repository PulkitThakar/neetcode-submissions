class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.running_sum = [0]
        for i in w:
            self.running_sum.append(self.running_sum[-1] + i)


    def pickIndex(self) -> int:
        target = random.random() * self.running_sum[-1]
        l, r = 0, len(self.running_sum) - 1
        while l < r:
            m = l + ((r-l)//2)
            if self.running_sum[m] <= target:
                l = m + 1
            else:
                r = m
        return l - 1

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()