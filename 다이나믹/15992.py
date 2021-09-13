t = int(input())
maxValue = 0
numList=[]
for _ in range(t):
    n, m = map(int,input().split())
    numList.append([n,m])
    maxValue = max(n,maxValue)

dp = [[0 for _ in range(maxValue+1)]  for _ in range(maxValue+1)]
dp[1][1] = 1
dp[2][1] = 1
dp[2][2] = 1
dp[3][1] = 1
dp[3][2] = 2
dp[3][3] = 1

for k in range(4, maxValue+1):
    for x in range(1, k+1):
        dp[k][x] = (dp[k-3][x-1] + dp[k-2][x-1] + dp[k-1][x-1]) % 1000000009

for n,m in numList:
    print(dp[n][m])