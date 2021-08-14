n, k = list(map(int, input().split()))
arr = [int(input()) for _ in range(n)]

dp = [0] *(k+1) #인덱스를 편의를 위해
dp[0] = 1 # (n==k일때 ) ex) 5원짜리로 5원 만드는 경우 1가지 

for i in arr:
    for j in range(i, k+1): #n원을 가지고 j원을 만들 수 있는 경우의 수
        dp[j] += dp[j-i]

print(dp[k])


