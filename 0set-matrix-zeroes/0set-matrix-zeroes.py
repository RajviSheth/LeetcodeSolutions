class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowZero = False
        
        rows = len(matrix)
        cols = len(matrix[0])
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    
                    if row > 0:
                        matrix[row][0] = 0
                        
                    else:
                        rowZero = True
                        
        
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0
                    
        
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0
                
        if rowZero:
            for c in range(cols):
                matrix[0][c] = 0
            