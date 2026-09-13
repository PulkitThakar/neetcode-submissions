class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line, length = [], 0
        i = 0
        while i < len(words):
            if length + len(line) + len(words[i]) > maxWidth:
                extra_space = maxWidth - length;

                space = extra_space // (max(1, len(line) - 1))
                remainder = extra_space % (max(1, len(line) - 1))

                for j in range(max(1, len(line) - 1)):
                    line[j] += " "*space
                    if remainder:
                        line[j] += " "
                        remainder -= 1
                res.append("".join(line))
                line, length = [], 0

            # continuing the line
            line.append(words[i])
            length += len(words[i])
            i += 1
        
        # last line
        extra_space = maxWidth - length - (len(line) - 1)
        res.append(" ".join(line) + " "*extra_space)
        return res