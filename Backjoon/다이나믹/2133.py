n = int(input())

dp = [0] * 30

dp[2] = 3

for i in range(3,n+1):
    if i % 2 == 0:
        dp[i] += dp[i-2] * 2 

print(dp[n])
