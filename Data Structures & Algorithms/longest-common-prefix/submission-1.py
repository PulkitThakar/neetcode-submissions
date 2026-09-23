class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        largest = float("inf")
        for i in strs:
            if len(i) < largest:
                res = i
        
        for i in strs:
            while res != i[:len(res)]:
                res = res[:-1]
            if res == "":
                return ""
        return res