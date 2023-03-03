input = open(0).readline
def solution():
    N = int(input())
    
    # sum = 0
    # for i in input().strip():
    #     sum += int(i)
    # print(sum) 
    
    # 이게 더 좋은듯
    print(sum([int(i) for i in input().strip()]))
        

if __name__ == '__main__': 
    solution()