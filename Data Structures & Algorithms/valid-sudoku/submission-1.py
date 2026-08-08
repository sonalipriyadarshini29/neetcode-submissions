class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def notValid(arr):
            nums = [x for x in arr if x!="."]
            return len(nums)==len(set(nums))

        for row in board:
            if notValid(row)==False:
                return False

        cols = zip(*board)
        for col in cols:
            if notValid(col)==False:
                return False

        grid = defaultdict(list)
        for r in range(0,9):
            for c in range(0,9):
                grid[(r//3,c//3)].append(board[r][c])
        for g in grid.values():
            if notValid(g)==False:
                return False
        return True