class Solution:
    def __init__(self):
        self.result = 0
        self.dx, self.dy = [1, 0, -1, 0], [0, -1, 0, 1]
        self.visited = []

    def numIslands(self, grid: List[List[str]]) -> int:
        self.visited =  [[False]* len(grid[0]) for _ in range(len(grid))]
    
        cnt = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if not self.visited[row][col] and grid[row][col] == "1":
                    self.dfs(grid, row, col)
                    cnt += 1
        return cnt
                                

    def dfs(self, grid, row, col):
        global visited
        self.visited[row][col] = True
        
        for i in range(4):
            new_row, new_col = row + self.dx[i], col + self.dy[i]
            
            if 0<= new_row <len(grid) and 0<= new_col < len(grid[0]) and not self.visited[new_row][new_col] and grid[new_row][new_col] == "1":
                self.dfs(grid, new_row, new_col)
        