# 풀이 1
# from copy import deepcopy
# T = int(input())
# for _ in range(T):
#     cycle = 0

#     N = int(input())
#     Ci = list(map(int, input().split()))

#     while True:
#         for candy in range(N):
#             if Ci[candy] % 2: # 홀수를 짝수로 만든다.
#                 Ci[candy] +=1

#         # 동일한 사탕수를 가질 때 까지!
#         is_same = True
#         for candy in range(N-1):
#             if Ci[candy] != Ci[candy+1]:
#                 is_same = False
#                 break
        
#         if is_same:
#             break
#         else: 
#             # 사탕돌리기 시작
#             # 1. 절반만큼 나눠
#             for candy in range(N):
#                 Ci[candy] = int(Ci[candy]/2)

#             temp = deepcopy(Ci)
#             # 2. 나눈만큼 오른쪽 애한테 줘
#             for candy in range(N):  
#                 if candy == N-1:
#                     Ci[0] += temp[candy]
#                 else:
#                     Ci[candy + 1] += temp[candy]
        
#         cycle += 1
#     print(cycle)


# 풀이 2

def check(N, candy):
    # 짝수개로 만들어주기
    for i in range(N):
        if candy[i] % 2:
            candy[i] += 1

    # 나머지가 같은지 체크 
    # candy배열을 set으로 만들면 중복이 모두 사라지니 1개만 남을 것.. 와 신박해
    return len(set(candy)) == 1 


def teacher(N, candy):
    tmp_lst = [0 for i in range(N)] # 오른쪽으로 전달해줘야 할 사탕의 개수
    for idx in range(N):
        if candy[idx] % 2:
            candy[idx] += 1

        candy[idx] //= 2
        tmp_lst[(idx + 1) % N] = candy[idx]
    
    for idx in range(N):
        candy[idx] += tmp_lst[idx]

    return candy



def process():
    N, candy = int(input()), list(map(int, input().split()))
    cnt = 0

    while not check(N, candy):
        cnt += 1
        candy = teacher(N, candy)
    
    print(cnt)


for i in range(int(input())):
    process()
