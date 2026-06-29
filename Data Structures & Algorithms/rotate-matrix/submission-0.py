class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)
        f, l = 0, N - 1
        print(f)
        print(l)

        while f < l:
            for i in range(l-f):
                print(i)
                temp = matrix[f][f+i]
                matrix[f][f+i] = matrix[l-i][f]
                matrix[l-i][f] = matrix[l][l-i]
                matrix[l][l-i] = matrix[f+i][l]
                matrix[f+i][l] = temp
            f += 1
            l -= 1