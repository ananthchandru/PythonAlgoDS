import collections

class ValidSudoku:
    def isValidSudoku(self, matrix: [[str]])->bool:

        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                if matrix[i][j] == ".":
                    continue
                if matrix[i][j] in rows[i] or\
                    matrix[i][j] in cols[j] or\
                    matrix[i][j] in squares[(i//3,j//3)]:
                    return False
                rows[i].add(matrix[i][j])
                cols[j].add(matrix[i][j])
                squares[(i//3,j//3)].add(matrix[i][j])

        return True

obj = ValidSudoku()

sudokuBoard1 = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

sudokuBoard2 = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(obj.isValidSudoku(sudokuBoard1))
print(obj.isValidSudoku(sudokuBoard2))