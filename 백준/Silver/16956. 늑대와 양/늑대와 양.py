import sys
from sys import stdin
sys.setrecursionlimit(10000)
input = stdin.readline


def solution1():
    R, C = map(int, input().split())
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

    farm = [list(map(str, input().strip())) for _ in range(R)]

    doom = False

    for row in range(R):
        for col in range(C):
            if farm[row][col] == "W":
                for i in range(4):
                    new_x, new_y = row + dx[i], col + dy[i]
                    if new_x < 0 or new_y < 0 or new_x == R or new_y == C:
                        continue
                    if farm[new_x][new_y] == "S":
                        doom = True
                    elif farm[new_x][new_y] == ".":
                        farm[new_x][new_y] = "D"


    if doom:
        print(0)
    else:
        print(1)
        for i in farm:
            print("".join(i))


def solution2():
    R, C = map(int, input().split())
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

    farm = [list(map(str, input().strip())) for _ in range(R)]

    doom = False

    for row in range(R):
        for col in range(C):
            if farm[row][col] == "W":
                for w in range(4):
                    new_row, new_col = row + dx[w], col + dy[w]
                    if new_row < 0 or new_row == R or new_col < 0 or new_col == C:
                        continue
                    if farm[new_row][new_col] == "S":
                        doom = True

    if doom:
        print(0)
    else:
        print(1)
        for i in range(R):
            for j in range(C):
                if farm[i][j] not in 'SW':
                    farm[i][j] = 'D'
        
        for i in farm:
            print(''.join(i))
            

if __name__ == '__main__': 
    # solution1()
    solution2()
        