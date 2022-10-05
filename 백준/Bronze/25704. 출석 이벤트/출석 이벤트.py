from re import L
from sys import stdin
input = stdin.readline

# sys.setrecursionlimit(10000000)

def solution():
    N = int(input())
    P = int(input())
    dc_price = []
    
    if N > 4:
        dc_price.append(500)
    if N > 9:
        dc_price.append(int(P//10))
    if N > 14:
        dc_price.append(2000)
    if N > 19:
        dc_price.append(int(P//4))

    # stamp의 개수가 없는 경우 dc_price = [] 빈 리스트가 된다.
    # 이럴 경우 max([])을 하면 에러가 발생함. 그것때문에 if dc_price else 0 을 붙여주어야 하는 것
    dc_price_result = max(dc_price) if dc_price else 0

    if (P > dc_price_result):
        return P - dc_price_result
    
    else:
        return 0



if __name__ == '__main__': 
    print(solution())