from sys import stdin
input = stdin.readline

def solution():
    T = int(input())
    for i in range(T):
        A, B = map(int, input().split())
        print(f"Case #{i+1}: {A+B}")
if __name__ == '__main__': 
    solution()

