class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res_len = (len(num1) + len(num2))
        res = [0] * res_len

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                k = i + j + 1
                z = int(num1[i]) * int(num2[j]) + res[k]
                res[k] = z % 10
                res[k - 1] += z // 10


                
        r = ""
        i = 0
        while i < res_len and res[i] == 0:
            i += 1
        while i < res_len:
            r += str(res[i])
            i += 1
        return r if r else "0"