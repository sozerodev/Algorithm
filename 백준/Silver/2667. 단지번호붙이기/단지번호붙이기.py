# launch.json은 커서가 존재하는 파일을 기준으로 실행됩니다.
# 다음과 같이 예시를 넣으면 mySettings/input.txt 의 input값을 읽어
# output.txt에서 출력이 됩니다.
from collections import deque
from logging import exception
import sys
from sys import stdin
input = stdin.readline

# sys.setrecursionlimit(10000000)

M = deque([])
visit = []
num = 0

def dfs(x, y):
    global M, visit, num

    if M[x][y] == 0 or visit[x][y]:
        return
    visit[x][y] = 1

    if M[x][y]:
        num += 1


    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

    for i in range(4):
        new_x, new_y = x + dx[i], y + dy[i]

        if M[new_x][new_y] == 0:
            continue
        
        
        # num += 1
        dfs(new_x, new_y)




def solution():
    global M, visit, num
    N = int(input())

    M = deque([ deque(map(int, input().strip())) for _ in range(N)])
    visit = [[0] * (N+2) for _ in range (N*2)]
    # 끝부분에 모두 0 을 추가해놔야 나중에 dfs에서 index out of range가 나오지 않는다.
    M.appendleft(deque([0])*N)
    M.append(deque([0])*N)
    for i in M:
        i.appendleft(0)
        i.append(0)


    
    apt_num = 0
    result = {}
    for row in range(1, N + 1):
        for col in range(1, N + 1):
            if M[row][col] == 0 or visit[row][col]:
                continue
            else:
                dfs(row, col)
                apt_num += 1
                result[apt_num] = num
                num = 0
                
    
    print(len(result.keys()))
    for value in sorted(result.values()):
        print(value)


if __name__ == '__main__': 
    solution()