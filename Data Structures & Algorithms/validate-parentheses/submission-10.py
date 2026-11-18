class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for i in s:
            if i in ("(", "{", "["):
                stk.append(i)
            elif not stk:
                return False
            elif i == ")" and stk[-1] == "(":
                stk.pop()
            elif i == "}" and stk[-1] == "{":
                stk.pop()
            elif i == "]" and stk[-1] == "[":
                stk.pop()
            else:
                return False
        
        return len(stk) == 0