# 풀이 1 (상황에 따른 올바른 자료형 사용.. 파이썬에는 dictionary, hash, set..같은 자료형을 활용하자)
# 풀이 1-1
# import sys

# N, A_arr = sys.stdin.readline(), set(map(int, sys.stdin.readline().split())) # 탐색할 땐 list보다 set자로형이 훨씬 빠르다.
# M, arr = sys.stdin.readline(), list(map(int, sys.stdin.readline().split()))


# for num in arr:
#     if num in A_arr:
#         print(1)
#     else:
#         print(0)


# 풀이 1-2
N, A = int(input()), {i: 1 for i in map(int, input().split())}
M = input() # 필요 없으니 그냥 스킵

for i in list(map(int, input().split())):
    print(A.get(i, 0)) # A라는 dictionary 객체에서 i라는 키를 뽑되, 없으면 0으로 채워넣는다. 
    # print(1 if i in A else 0) # 다음과 같이도 사용 가능



# 풀이2 (이분탐색 활용)
# 특정 알고리즘을 요구한다고 하여 꼭 그 알고리즘대로 풀 필요는 없다. 코테는 그러한 허점이 있고 
# 자료구조를 잘 파악하여 그 허점을 파고드는 것이 좋다.  
# 이런 문제에서는 파이썬의 장점을 잘 활용하는 것이 좋다. 


