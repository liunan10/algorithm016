class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.rows = [set(range(1, 10)) for _ in range(9)]
        self.columns = [set(range(1, 10)) for _ in range(9)]
        self.boxes = [set(range(1, 10)) for _ in range(9)]

        self.target = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = int(board[i][j])
                    self.rows[i].remove(num)
                    self.columns[j].remove(num)
                    boxIndex = (i // 3) * 3 + j // 3
                    self.boxes[boxIndex].remove(num)
                else:
                    self.target.append((i, j))
        self.dfs(board, 0)

    def dfs(self, board, curr):
        if curr == len(self.target):
            return True
        i, j = self.target[curr]
        b = (i // 3) * 3 + j // 3
        for num in self.rows[i] & self.columns[j] & self.boxes[b]:
            self.rows[i].remove(num)
            self.columns[j].remove(num)
            self.boxes[b].remove(num)
            board[i][j] = str(num)
            if self.dfs(board, curr + 1):
                return True
            self.rows[i].add(num)
            self.columns[j].add(num)
            self.boxes[b].add(num)
        

        
