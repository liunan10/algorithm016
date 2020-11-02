# boxIndex = (i // 3) * 3 + (j // 3)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = [{} for _ in range(9)]
        rows = [{} for _ in range(9)]
        boxes = [{} for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    value = int(board[i][j])
                    rows[i][value] = rows[i].get(value, 0) + 1
                    columns[j][value] = columns[j].get(value, 0) + 1
                    boxIndex = (i // 3) * 3 + (j // 3)
                    boxes[boxIndex][value] = boxes[boxIndex].get(value, 0) + 1
                    if rows[i][value] > 1 or columns[j][value] > 1 or boxes[boxIndex][value] > 1: return False

        return True 
