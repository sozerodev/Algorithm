# launch.json은 커서가 존재하는 파일을 기준으로 실행됩니다.
# 다음과 같이 예시를 넣으면 mySettings/input.txt 의 input값을 읽어
# output.txt에서 출력이 됩니다.
import sys
from sys import stdin
input = stdin.readline

# dfs 를 쓸 때 필요함
# sys.setrecursionlimit(10000)

def solution():
    print()


if __name__ == '__main__': 
    solution()