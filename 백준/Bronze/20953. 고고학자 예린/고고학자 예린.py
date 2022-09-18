import sys

if __name__ == '__main__': 
    T = int(input())
    for _ in range(T):
        a, b = map(int, sys.stdin.readline().split())
        print((a + b)**2*(a + b -1)//2)