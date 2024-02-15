class Solution:
    def matrixMedian(self, grid: List[List[int]]) -> int:
        res = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                res.append(grid[row][col])
        
        res.sort()
        n = len(res)
        median = n // 2
        return res[median]
        