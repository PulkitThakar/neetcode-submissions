class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        numToLetters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        res = []
        combination = ""

        def backtracking(i: int):
            nonlocal combination

            if i == len(digits):
                res.append(combination[:])
                return
            
            for l in numToLetters[digits[i]]:
                combination += l
                backtracking(i + 1)
                combination = combination[: -1]
        
        backtracking(0)
        return res