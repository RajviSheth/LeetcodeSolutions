class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target in row:
                return True
            
        return False
        
#         ROWS, COLS= len(matrix), len(matrix[0])
#         top, bot = 0, ROWS-1
        
#         while top <= bot:
#             row = (top+bot)//2
#             if target > matrix[row][-1]:
#                 top
        