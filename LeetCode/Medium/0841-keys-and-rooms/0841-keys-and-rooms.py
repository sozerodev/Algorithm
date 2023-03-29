from collections import deque

class Solution:
    def __init__(self) -> None:
        self.visited = []

    def bfs(self, start_v, rooms):
        self.visited[start_v] = True
        
        queue = deque()
        queue.append(start_v)
        
        while queue:
            cur_v = queue.popleft()
            
            for v in rooms[cur_v]:
                if not self.visited[v]:
                    self.visited[v] = True
                    queue.append(v)
        
        
    def dfs(self, cur_v, rooms):
        self.visited[cur_v] = True
        
        for v in rooms[cur_v]:
            if not self.visited[v]:
             self.dfs(v, rooms)
        
        
    def canVisitAllRooms(self, rooms) -> bool:
        self.visited = [False for _ in range(len(rooms))]
        self.visited[0] = True
        
        for v in rooms[0]:
            #self.dfs(v, rooms)
            self.bfs(v, rooms)
            
            
        if self.visited.count(False) == 0:
            return True
        else:
            return False
        
        
        