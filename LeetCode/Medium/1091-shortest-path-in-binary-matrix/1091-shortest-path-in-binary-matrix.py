class Solution:
    def __init__(self) -> None:
        self.visited = []
        self.dx, self.dy = [0, 1, 1, 1, 0, -1, -1, -1], [1, 1, 0, -1, -1, -1, 0, 1]
        
        
    def shortestPathBinaryMatrix(self, grid) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        shortest_path_length = -1
        
        row, col = len(grid), len(grid[0])
        self.visited = [[False]* col for _ in range(row)]

        # (0, 0) 방문 예약! 
        queue = deque() # 1은 현재 길이
        queue.append((0, 0, 1))
        self.visited[0][0] = True
        
        
        while queue:
            cur_row, cur_col, cur_length = queue.popleft()
            
            # 목적지에 도착했을 때 그때의 cur_length를 shortest_path_length에 저장한다.
            if cur_row == row-1 and cur_col == col-1:
                shortest_path_length = cur_length
                break
            
            for i in range(8):
                new_row, new_col = cur_row + self.dx[i], cur_col + self.dy[i]
                
                if 0<= new_row < row and 0<= new_col < col and not self.visited[new_row][new_col] and grid[new_row][new_col] == 0:
                    self.visited[new_row][new_col] = True
                    queue.append((new_row, new_col, cur_length + 1))
                    
        
        return shortest_path_length