from collections import deque
input = open(0).readline

# dfs 를 쓸 때 필요함
# sys.setrecursionlimit(10000)

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

def dfs(x, y):
    global graph, visited
    
    if not (0 <= x <N and 0 <= y < M) or visited[x][y]: return
    
    visited[x][y] = 1
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if not (0 <= nx <N and 0 <= ny < M): continue
        if graph[nx][ny] == 0 or visited[nx][ny]:
            continue
            
        dfs(nx, ny)
        
        
def bfs(x, y):
    global graph, visited, N, M
    
    q = deque([(x, y)])
    
    while q:
        x, y = q.pop()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0<= nx <N and 0<= ny < M and graph[nx][ny] == 1 and visited[nx][ny] != 1:
                q.append((nx, ny))
                visited[nx][ny] = 1
    return 1
                

if __name__ == '__main__':
    T = int(input())
    
    for _ in range(T):
        M, N, K = map(int, input().split())
        
        graph = [[0]*(M) for _ in range (N)]
        visited = [[0]*(M) for _ in range(N)]
        ans = 0
        
        for _ in range (K):
            x, y = map(int, input().split())
            graph[y][x] = 1
    

        for i in range(0, M):
            for j in range(0, N):
                if graph[j][i] == 0 or visited[j][i]:
                    continue
                
                # dfs(j, i)
                # ans += 1
                
                ans += bfs(j, i)
                
        print(ans)

    
    