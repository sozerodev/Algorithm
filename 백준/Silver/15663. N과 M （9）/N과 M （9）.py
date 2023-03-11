from itertools import permutations
input = open(0).readline

def solution():
    N, M = map(int, input().split())
    lst = sorted(list(map(int, input().split())))
    lst = set(permutations(lst, M))
    
    for per in sorted(lst):
        print(*per)

if __name__ == '__main__': 
    solution()