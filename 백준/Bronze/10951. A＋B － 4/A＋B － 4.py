from sys import stdin
input = stdin.readline

def solution():
    try:
        while True:
            A, B = map(int, input().split())
            print(A+B)
    except:
        return

if __name__ == '__main__': 
    solution()

