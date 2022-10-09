from sys import stdin
import sys
input = stdin.readline

sys.setrecursionlimit(10000000)

paint = [] 
visit = []
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def solution():
    global paint,visit

    # 1. 입력정보 받기
    N = int(input())
    paint = [list(input().strip()) for _ in range(N)]

    # 정상, 적록색약
    normal, abnormal = 0, 0

    # 정상
    visit = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0:
                visit[i][j] = 1
                dfs(i, j, paint[i][j])
                cnt += 1

    
    print(cnt, end=" ")
    # 적록색약
    visit = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0:
                visit[i][j] = 1
                dfs(i, j, paint[i][j])
                cnt += 1
    
    print(cnt)


def dfs(x, y, alphabet):
    global paint, visit, dx, dy

    # 적록색약을 구하기 위해 빨강을 초록으로 바꿔주기
    if alphabet == "R":
        paint[x][y] = "G"

    for i in range(4):
        new_x, new_y = x + dx[i], y + dy[i]

        if -1<new_x<len(visit) and -1<new_y<len(visit) and visit[new_x][new_y] == 0 and paint[new_x][new_y] == alphabet:
            visit[new_x][new_y] = 1
            dfs(new_x, new_y, alphabet)

if __name__ == '__main__': 
    solution()
