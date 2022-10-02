import sys
from sys import stdin
sys.setrecursionlimit(10000)
input = stdin.readline

ground, chk = [], []


def dfs(x, y):
    # 방향벡터!
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
    global ground, chk

    if (chk[x][y]):
        return
    
    chk[x][y] = 1

    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if ground[xx][yy] == 0 or chk[xx][yy]:
            continue

        dfs(xx, yy)





def solution():
    global ground, chk

    M, N, K = map(int, input().split())

    # 상하좌우를 각각 한칸씩 더 채워주자. 값이 비어있으면 곤란하니까. 
    ground = [ [0] * (50 + 2) for _ in range (50 + 2)]
    chk = [ [0] * (50 + 2) for _ in range (50 + 2)] 

    # 배추의 위치 
    for _ in range(K):
        X, Y = map(int, input().split())
        ground[Y + 1][X + 1] = 1

    ans = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if ground[i][j] == 0 or chk[i][j]:
                continue
                 
            dfs(i, j)
            ans += 1
 
    print(ans)


    
if __name__ == '__main__': 
    T = int(input())
    for _ in range(T):
        solution()
        