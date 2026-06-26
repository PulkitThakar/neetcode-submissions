class Solution:
    def checkValidString(self, s: str) -> bool:
        minn = 0
        maxx = 0
        
        for i in s:
            if i == '(':
                minn += 1
                maxx += 1
            elif i == ")":
                minn -= 1
                maxx -= 1
                if maxx < 0:
                    return False
            else:
                minn -= 1
                maxx += 1
            minn = max(minn, 0)
        
        return minn == 0
            
