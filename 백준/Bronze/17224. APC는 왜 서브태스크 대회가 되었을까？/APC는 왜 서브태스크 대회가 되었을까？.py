N, L, K = map(int, input().split())

score, sub1, sub2 = 0, 0, 0
for q in range(N):
    sub1_q, sub2_q = map(int, input().split())
    
    if L >= sub2_q:
        sub2 += 1
    elif L >= sub1_q and L < sub2_q :
        sub1 += 1
    
if sub1 + sub2 > K:
    while True:
        if sub1 > 0:
            sub1 -= 1
        else:
            sub2 -= 1

        if sub1 + sub2 <= K:
            break
    
print(sub1*100 + sub2*140)
