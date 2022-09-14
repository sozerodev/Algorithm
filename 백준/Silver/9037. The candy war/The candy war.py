from copy import deepcopy

T = int(input())
for _ in range(T):
    cycle = 0

    N = int(input())
    Ci = list(map(int, input().split()))

    while True:
        for candy in range(N):
            if Ci[candy] % 2: # 홀수를 짝수로 만든다.
                Ci[candy] +=1

        # 동일한 사탕수를 가질 때 까지!
        is_same = True
        for candy in range(N-1):
            if Ci[candy] != Ci[candy+1]:
                is_same = False
                break
        
        if is_same:
            break
        
        if (not is_same):
            # 사탕돌리기 시작
            # 1. 절반만큼 나눠
            for candy in range(N):
                Ci[candy] = int(Ci[candy]/2)

            temp = deepcopy(Ci)
            # 2. 나눈만큼 오른쪽 애한테 줘
            for candy in range(N):  
                if candy == N-1:
                    Ci[0] += temp[candy]
                else:
                    Ci[candy + 1] += temp[candy]
        
        cycle += 1
    print(cycle)