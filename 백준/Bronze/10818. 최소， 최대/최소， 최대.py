input = open(0).readline

def solution():
    N = int(input())
    lst = list(map(int, input().split()))
    print(f"{min(lst)} {max(lst)}")
    
if __name__ == '__main__': 
    solution()