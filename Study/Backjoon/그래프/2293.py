n, k = map(int, input().split())
dp = [0] * (k+1)
count = 0
coins = [int(input()) for _ in range(n)]
dp[0] = 1
for i in coins:
    for j in range(i, k+1):
        dp[j] += dp[j-i]

print(dp)
