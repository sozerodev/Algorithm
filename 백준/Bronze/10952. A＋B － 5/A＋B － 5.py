from sys import stdin
input = stdin.readline

def solution():
    while True:
        A, B = map(int, input().split())
        if (A != 0 or B != 0):
            print(A+B) 
        else:
            return

if __name__ == '__main__': 
    solution()

