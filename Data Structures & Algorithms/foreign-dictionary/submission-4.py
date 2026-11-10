class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}

        for i in range(len(words) - 1):
            word = words[i]
            next_word = words[i + 1]
            min_len = min(len(word), len(next_word))
            if (
                len(word) > len(next_word)
                and word[:min_len] == next_word[:min_len]
            ):
                print("hi")
                return ""
            
            for c_idx in range(min_len):
                if word[c_idx] != next_word[c_idx]:
                    adj[word[c_idx]].add(next_word[c_idx])
                    break
        
        visit = set()
        loop = set()
        res_lex = []
        def dfs(curr_node):
            if curr_node in loop:
                return False
            if curr_node in visit:
                return True
            
            visit.add(curr_node)
            loop.add(curr_node)
            for nei in adj[curr_node]:
                if not dfs(nei):
                    return False
            loop.remove(curr_node)
            res_lex.append(curr_node)
            return True
        
        for c in adj:
            if c not in visit:
                if not dfs(c):
                    return ""
        
        return "".join(reversed(res_lex))