input = open(0).readline
def solution():
    
    # N = int(input())
    # for i in range(N):
    #     print(i + 1)
    
    # simple way
    print("\n".join(map(str, range(1, int(input())+1))))

if __name__ == '__main__': 
    solution()