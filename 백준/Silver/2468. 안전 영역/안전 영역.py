from sys import stdin
import sys
input = stdin.readline

sys.setrecursionlimit(10000000)

region = [] # region은 전역으로
visit = []
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def solution():
    global region,visit

    # 1. 입력정보 받기
    N = int(input())
    region = [list(map(int, input().split())) for _ in range(N)]

    # 2. 높이가 가장 낮은 지역과 높은 지역 구하기
    min_height, max_height = 100, 1 # 높이는 1이상, 100이하의 정수 (조건에 높이는 1이상, 100이하)
    for i in range(N):
        for j in range(N):
            min_height = min(min_height, region[i][j])
            max_height = max(max_height, region[i][j])
    
    # 2-1. 수심에 따른 침수지역 정보를 담을 리스트 받기 (어차피 최대 개수만 알면 되니 리스트를 사용)
    flooded_area_num = []

    # 3. 안전영역 최대 개수 구하기
    for height in range(min_height, max_height): # max_height이하로는 모두 침수대상이니 +1 해줄 필요 없다
        visit = [[0]*N for _ in range(N)] # 방문지역
        cnt = 0 # dfs끝날 때마다 증가시킬 변수, 즉 침수되지 않은 지역군

        for i in range(N):
            for j in range(N):
                if region[i][j] > height and not visit[i][j]: 
                    visit[i][j] = 1
                    cnt += 1
                    dfs(i, j, height)
        flooded_area_num.append(cnt)
        
    # 아무 지역도 물에 잠기지 않을 수 있다.
    print(max(flooded_area_num)) if len(flooded_area_num) > 0 else print(1)

def dfs(x, y, height):
    global region, visit, dx, dy
    
    for i in range(4):
        new_x, new_y = x + dx[i], y + dy[i]
        if -1<new_x<len(visit) and -1<new_y<len(visit) and not visit[new_x][new_y] and region[new_x][new_y] > height :
            visit[new_x][new_y] = 1
            dfs(new_x, new_y, height)
    


if __name__ == '__main__': 
    solution()
