class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        grid = defaultdict(set)

        for r in range(9):
            for c in range(9):
                # if it's empty, then just continue
                if board[r][c] == ".":
                    continue
                
                # if the number exist in a row, 
                # col, or grid, return false
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or
                    board[r][c] in grid[(r // 3, c // 3)]):
                    return False
                
                # if the number not exist, 
                # add it to the rows, cols and grid hashmaps
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                grid[(r // 3, c // 3)].add(board[r][c])
        return True
