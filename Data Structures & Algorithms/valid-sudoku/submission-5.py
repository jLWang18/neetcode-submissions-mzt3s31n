class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # dict_row, col, grid.
        dict_row, dict_col, dict_grid = defaultdict(set), defaultdict(set), defaultdict(set)

        # loop the board
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == '.':
                    continue
    
                val = board[i][j]
                # if this number in dict_row, col, grid already return False
                if (val in dict_row[i] or 
                    val in dict_col[j] or
                    val in dict_grid[(i//3, j//3)]):
                   return False
                # if not, add to each dict.
                dict_row[i].add(val)
                dict_col[j].add(val)
                dict_grid[(i//3, j//3)].add(val)
        return True
