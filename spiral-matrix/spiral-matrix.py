class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = 0
        right = len(matrix[0])
        top = 0
        bottom = len(matrix)
        res = []
        
        while left < right and top < bottom:
            # get top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            # get right column
            for i in range(top, bottom):
                res.append(matrix[i][right -1])
            right -= 1
            
            if not (left < right and top < bottom):
                break
            # get bottom row
            for i in range(right-1, left -1, -1):
                res.append(matrix[bottom - 1][i])
            bottom  -= 1
            # get left col
            for i in range(bottom-1, top -1, -1):
                res.append(matrix[i][left])
            left += 1
            
        return res