class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_par = set(['[', '(', '{'])
        for i in s:
            if i in open_par:
                stack.append(i)
            elif (
                stack and (
                    (i == ']' and stack[-1] == '[')
                    or (i == ')' and stack[-1] == '(')
                    or (i == '}' and stack[-1] == '{')
                )
            ):
                stack.pop()
            else:
                return False
        
        return len(stack) == 0