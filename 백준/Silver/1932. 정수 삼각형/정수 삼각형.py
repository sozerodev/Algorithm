from sys import stdin
input = stdin.readline

def solution():
    global lst, n, sum
    N = int(input())
    # Dp[i][j] : i, j 도착했을 때 최댓값
    # Dp[i][j] : max(Dp[i-1][j-1], Dp[i-1][j]) + A[i][j]
    A = [[0 for _ in range(N + 1)]for i in range(N + 1)]
    DP = [[0 for _ in range(N + 1)] for i in range(N + 1)]

    # lst = [list(map(int, input().split())) for _ in range(n)]    
    for i in range(1, N + 1):
        tmp = list(map(int, input().split()))
        for j in range(1, i + 1):
            A[i][j] = tmp[j - 1]

    for i in range(1, N + 1):
        for j in range(1, i + 1):
            DP[i][j] = max(DP[i - 1][j - 1], DP[i - 1][j]) + A[i][j]
 
    print(max(DP[-1]))

if __name__ == '__main__': 
    solution()