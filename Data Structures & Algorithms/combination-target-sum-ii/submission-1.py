class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        curr = []

        def backtracking(i, target):
            if target == 0:
                res.append(curr[:])
                return
            if target < 0 or i >= len(candidates):
                return
            
            curr.append(candidates[i])
            backtracking(i + 1, target - candidates[i])
            curr.pop()
            j = i + 1
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            backtracking(j, target)
        
        backtracking(0, target)
        return res