class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        minRow, maxRow, minCol, maxCol = row1, row2, col1, col2
        summ = 0
        for r in range(minRow, maxRow+1):
            for c in range(minCol, maxCol+1):
                summ += self.matrix[r][c]
        return summ


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)