class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count =0
        n= len(grid)
        for i in range(n):
            row=grid[i]
            for j in range(n):
                col= [grid[row][j] for row in range(n)]
                if row== col:
                    count+=1
        return count 

