from collections import deque
import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    cnt = 0
    for i in range(N-1, 0, -1):
        max_idx = A.index(max(A[:i+1]))
        
        if i != max_idx:       
            A[i], A[max_idx] = A[max_idx], A[i]
            cnt += 1
        if cnt == K:
            print(f"{A[max_idx]} {A[i]}")
            sys.exit(0)
    print(-1)
            
    

    