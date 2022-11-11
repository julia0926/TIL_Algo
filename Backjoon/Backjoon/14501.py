# https://www.acmicpc.net/problem/14501
n = int(input())
schedule = []
for i in range(n):
    schedule.append(list(map(int, input().split())))

dp = [0 for _ in range(n+1)]
#logic
for i in range(n-1, -1, -1): #뒤에서 부터 
    if i + schedule[i][0] > n:
        dp[i] = dp[i+1]
    else:
        #현재값 vs 이전 금액 + 옮겼을 때 금액
        dp[i] = max(dp[i+1], schedule[i][1] + dp[i + schedule[i][0]])

print(dp)