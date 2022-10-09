# launch.json은 커서가 존재하는 파일을 기준으로 실행됩니다.
# 다음과 같이 예시를 넣으면 mySettings/input.txt 의 input값을 읽어
# output.txt에서 출력이 됩니다.
import sys
from sys import stdin
input = stdin.readline

# dfs 를 쓸 때 필요함
# sys.setrecursionlimit(10000)

def solution():
    # 1. 값 받기
    N = int(input())
    card = list(map(int, input().split()))
    card.sort() # 해당 리스트에서 특정 요소가 존재하는지를 찾는 지표가 되니 정렬해준다. 

    M = int(input())
    has_num = list(map(int, input().split()))

    # 2. has_num의 요소가 card에 존재하는지를 확인
    for num in has_num:
        result = binary_search(card, num, 0, N-1) # 이분 탐색 
        if result != None:
            print(1, end = " ")
        else:
            print(0, end = " ")


def binary_search(array, target, start, end):
    while start < end + 1:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            # targe이 중간의 요소값보다 작다면 end를 중간값보다 하나 작은 범위로
            end = mid - 1
        else:
            # target이 중간의 요소값보다 크다면 start를 중간값보다 하나 큰 범위로
            start = mid + 1
        
    return None

if __name__ == '__main__': 
    solution()