from re import L
import sys
from sys import stdin
input = stdin.readline

# sys.setrecursionlimit(10000000)

matrix = []
visit = []


def dfs(x, y):
    global matrix, visit
    
    if matrix[x][y] == "1" or visit[x][y]:
        return
    visit[x][y] = 1

    dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]

    for i in range(4):
        new_x, new_y = x + dx[i], y + dy[i]

        if  0<= new_x < len(matrix) and 0<= new_y < len(matrix[0]) and visit[new_x][new_y] == 0 and matrix[new_x][new_y] == "0":
            dfs(new_x, new_y)


def solution():
    global matrix, visit
    N, M = map(int, input().split())

    for _ in range(N):
        matrix.append(list(input().rstrip()))
    visit = [[0] * M for _ in range(N)]

    cnt = 0
    for row in range(N):
        for col in range(M):
            if matrix[row][col] == "0" and visit[row][col] != 1 :
                dfs(row, col)
                cnt += 1

    print(cnt)

if __name__ == '__main__': 
    solution()