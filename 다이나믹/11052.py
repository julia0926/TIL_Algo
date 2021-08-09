N = int(input())
list = [0] + list(map(int, input().split())) #가격
dp = [0 for _ in range(N+1)] #카드 i개를 구매할 때 최대가격 

# N개인 경우의 수를 구해야함 
for i in range(1, N+1): 
    for j in range(1, i+1): 
        dp[i] = max(dp[i], dp[i-j] + list[j] )

print(dp[N])