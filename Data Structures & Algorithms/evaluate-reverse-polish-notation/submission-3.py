class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for i in tokens:
            if i == '+':
                temp1 = s.pop()
                temp2 = s.pop()
                s.append(temp2 + temp1)
            
            elif i == '-':
                temp1 = s.pop()
                temp2 = s.pop()
                s.append(temp2 - temp1)
            
            elif i == '*':
                temp1 = s.pop()
                temp2 = s.pop()
                s.append(temp2 * temp1)
            
            elif i == '/':
                temp1 = s.pop()
                temp2 = s.pop()
                temp = abs(temp2) // abs(temp1)
                if (temp1 < 0 and temp2 < 0) or (temp1 > 0 and temp2 > 0):
                    s.append(temp)
                else:
                    s.append(-temp)
            
            else:
                s.append(int(i))
            
            # print(s)
        
        return s[-1]