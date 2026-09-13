class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        n = len(words)
        res = []
        i = 0
        while i < n:
            j = i
            curr = 0
            for k in range(i, n):
                spaces = k - i
                if curr + spaces + len(words[k]) > maxWidth:
                    j = k
                    break
                curr += len(words[k])
                if k == n-1:
                    j = k + 1
            
            if j <= i + 1:
                res.append(f"{words[i]}{" "*(maxWidth - len(words[i]))}")
            elif j == n:
                spa = j - i - 1
                s_chars = maxWidth - curr
                r = words[j-1]
                for c in range(j - 2, i - 1, -1):
                    s = " "
                    r = words[c] + s + r
                
                    s_chars -= len(s)
                    spa -= 1
                r += " "*s_chars
                res.append(r)
            else:
                spa = j - i - 1
                s_chars = maxWidth - curr
                r = words[j-1]
                for c in range(j - 2, i - 1, -1):
                    s = " "*(s_chars // spa)
                    r = words[c] + s + r
                    
                    s_chars -= len(s)
                    spa -= 1
                
                res.append(r)


            i = j if j > i else i + 1
        
        return res