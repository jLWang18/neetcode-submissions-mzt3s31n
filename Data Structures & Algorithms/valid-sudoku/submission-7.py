class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                num = board[i][j]
                if num in row[i] or num in col[j] or num in box[(i // 3, j // 3)]:
                    return False
                row[i].add(num)
                col[j].add(num)
                box[(i // 3, j // 3)].add(num)
                print("row: " + str(row))
                print("col: " + str(col))
                print("box: " + str(box))
        return True