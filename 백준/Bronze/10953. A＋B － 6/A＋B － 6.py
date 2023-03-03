from sys import stdin
input = stdin.readline

def solution():
    T = int(input())
    for _ in range(T):
        A, B = map(int, input().split(","))
        print(A+B)

if __name__ == '__main__': 
    solution()

