class Solution:
    def __init__(self) -> None:
        self.visited = []

    def dfs(self, cur_v, rooms):
        self.visited[cur_v] = True
        
        for v in rooms[cur_v]:
            if not self.visited[v]:
             self.dfs(v, rooms)
        
        
    def canVisitAllRooms(self, rooms) -> bool:
        self.visited = [False for _ in range(len(rooms))]
        self.visited[0] = True
        
        for v in rooms[0]:
            self.dfs(v, rooms)

        if self.visited.count(False) != 0:
            return False
        else:
            return True