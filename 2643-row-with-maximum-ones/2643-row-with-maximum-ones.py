class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_count = 0
        row_num = 0
        for row in range(len(mat)):
            count = 0
            for col in range(len(mat[0])):
                if mat[row][col] == 1:
                    count += 1
            if count > max_count:
                max_count = count
                row_num = row
                
        return [row_num, max_count]
                    
        