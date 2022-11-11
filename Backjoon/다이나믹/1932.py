import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0 for i in range(j+1)] for j in range(n)]

dp[0][0] = arr[0][0]

for i in range(1, n): #1부터 시작 
    for j in range(i+1): #0부터 시작
        if j==0: #처음과 끝은 비교하지 않고 더함 (비교대상이 없음)
            dp[i][j] = dp[i-1][0] + arr[i][0]
        if j==i:
            dp[i][j] = dp[i-1][i-1] + arr[i][j]
        if 0<j<i:
            dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + arr[i][j]

print(max(dp[n-1]))