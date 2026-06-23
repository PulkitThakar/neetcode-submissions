class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        last, secondLast = 1, 1
        for i in range(n - 1, -1, -1):
            if s[i] =='0':
                secondLast = last
                last = 0
            elif (
                i < n - 1
                and (
                    s[i] == '1' or
                    (s[i] == '2' and '0' <= s[i+1] <= '6')
                    )
                ):
                temp = last + secondLast
                secondLast = last
                last = temp
            else:
                secondLast = last
        
        return last