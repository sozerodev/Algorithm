input = open(0).readline
N = int(input())

my_stack = []
for _ in range(N):
    do = input().strip()
    
    if do.startswith("push"):
        my_stack.append(int(do.split()[1]))
        
    elif do == "pop":
        if len(my_stack) == 0: 
            print(-1)
        else: 
            print(my_stack.pop())
        
    elif do=="size":
        print(len(my_stack))
        
    elif do=="empty":
        if len(my_stack) == 0: 
            print(1) 
        else: 
            print(0)
        
    elif do=="top":
        if len(my_stack) == 0: 
            print(-1)
        else: 
            print(my_stack[-1])
    
    