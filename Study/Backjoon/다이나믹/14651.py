N = int(input())

# 3의 배수 판별법 : 각 자리 숫자의 합이 3의 배수
# 0, 1, 2 만 사용 가능
dp = [0 for _ in range (N+2)] #1 하면 인덱스 에러  


dp[2] = 2
for k in range(3, N+1): 
    dp[k] = dp[k-1] * 3 % 1000000009

print(dp[N])
