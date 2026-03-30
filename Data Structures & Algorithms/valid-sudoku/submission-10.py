class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict = defaultdict(set)
        col_dict = defaultdict(set)
        grid = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                num = board[i][j]
                if num in row_dict[i] or num in col_dict[j] or num in grid[(i//3, j//3)]:
                    return False
                row_dict[i].add(num)
                col_dict[j].add(num)
                grid[(i//3, j//3)].add(num)
        return True