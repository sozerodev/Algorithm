input = open(0).readline
def solution():
    N = int(input())
    sum = 0
    for i in input().strip():
        sum += int(i)
       
    print(sum) 
if __name__ == '__main__': 
    solution()

