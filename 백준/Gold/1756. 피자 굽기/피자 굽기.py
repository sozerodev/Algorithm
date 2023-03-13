import sys
input = open(0).readline

if __name__ == '__main__':
    D, N = map(int, input().split())
    oven_lst = list(map(int, input().split()))
    dough_lst = list(map(int, input().split()))
    
    baked_pizza = [False] * N
    dough_idx = 0
    
    for i in range(1, D):
        oven_lst[i] = min(oven_lst[i], oven_lst[i-1])
    
    for oven_idx in range(D-1, -1, -1):
        if dough_lst[dough_idx] <= oven_lst[oven_idx]:
            dough_idx += 1
            
            if dough_idx >= N:
                print(oven_idx + 1)
                sys.exit(0)
            else:
                continue
        
    print(0)