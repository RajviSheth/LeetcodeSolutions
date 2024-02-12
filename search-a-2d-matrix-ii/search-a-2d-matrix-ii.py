class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        r, c = rows-1, 0
        
        while r >= 0 and c < cols:
            if target == matrix[r][c]:
                return True
            elif target > matrix[r][c]:
                c += 1
            else:
                r -= 1
        return False
        