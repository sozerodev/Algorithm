input = open(0).readline

# dfs 를 쓸 때 필요함
# sys.setrecursionlimit(10000)


def solution():
    
    # 풀이1. itertools를 사용한 풀이
    # N, M = map(int, input().split())
    # lst = sorted(list(map(int, input().split())))
    
    # from itertools import permutations  
    # lst = set(permutations(lst, M))
    # for per in sorted(lst):
    #     print(*per)
    
    
    # 풀이2. itertools없이 사용
    if len(temp) == m:
        print(*temp)
        return
    point_value = 0
    for i in range(n):
        if not visited[i] and point_value != nums[i]:
            visited[i] = True
            temp.append(nums[i])
            point_value = nums[i]
            solution()
            visited[i] = False
            temp.pop()


if __name__ == '__main__': 
    n, m = map(int, input().split())
    nums = sorted(list(map(int, input().split())))
    visited = [False] * n
    temp = []

    solution()