n, k = list(map(int, input().split()))
dp = [1 for _ in range(n+1)]

if n==k and k==0: #nCn이나 nC0은 1이므로 
    print(dp[1])
else:
    #팩토리얼 구하는 반복문 
    for i in range(2, n+1):
        dp[i] = dp[i-1] * i 
    print(dp[n] // (dp[k] * dp[n-k]) % 10007) #nCr 공식
