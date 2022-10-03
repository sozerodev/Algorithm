# launch.json은 커서가 존재하는 파일을 기준으로 실행됩니다.
# 다음과 같이 예시를 넣으면 mySettings/input.txt 의 input값을 읽어
# output.txt에서 출력이 됩니다.
from collections import deque
from logging import exception
from re import L
import sys
from sys import stdin
input = stdin.readline

# sys.setrecursionlimit(10000000)


def solution():

    N, M = map(int, input().split())
    miro = []
    queue = []
    dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]


    for i in range(N):
        miro.append(list(input().strip()))

        
    queue = [[0, 0]]
    miro[0][0] = 1
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < N and 0 <= y < M and miro[x][y] == "1":
                queue.append([x, y])
                miro[x][y] = miro[a][b] + 1


    print(miro[N - 1][M - 1])

if __name__ == '__main__': 
    solution()