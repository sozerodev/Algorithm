import sys

N, A_arr = sys.stdin.readline(), set(map(int, sys.stdin.readline().split()))
M, arr = sys.stdin.readline(), list(map(int, sys.stdin.readline().split()))


for num in arr:
    if num in A_arr:
        print(1)
    else:
        print(0)


