class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                k = i + j + 1
                z = int(num1[i]) * int(num2[j])
                while z:
                    z = res[k] + z
                    res[k] = z % 10
                    z = z // 10
                    k -= 1
        r = ""
        i = 0
        while i < (len(num1) + len(num2)) and res[i] == 0:
            i += 1
        while i < (len(num1) + len(num2)):
            r += str(res[i])
            i += 1
        return r if r else "0"