from sys import stdin
input = stdin.readline

def solution():
    while True:
        T = input().strip()
        if (T):
            print(T) 
        else:
            return
if __name__ == '__main__': 
    solution()

