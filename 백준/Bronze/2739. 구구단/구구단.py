input = open(0).readline
def solution():
    
    N = int(input())
    
    # for i in range(1, 10):
    #     print(f"{N} * {i} = {N*i}")
    print("\n".join(f"{N} * {i} = {N*i}" for i in range(1, 10)))
    
if __name__ == '__main__': 
    solution()