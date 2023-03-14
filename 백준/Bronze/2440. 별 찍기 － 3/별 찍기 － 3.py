N = int(input())

# 방법1
# for i in range(N, 0, -1):
#     print("*"*i)
    
# 방법2
for i in range(N):
    for j in range(N-i):
        print("*", end="")
    print()
        