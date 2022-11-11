n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
dp = [0] * (n+1)
#세번 연속 안됨, 한번에 세계단 안됨
if n == 1:
    print(arr[0])
elif n == 2:
    print(arr[1] + arr[0])
else:
    dp[0] = arr[0]
    dp[1] = arr[1] + arr[0]
    dp[2] = max(arr[0]+arr[2], arr[1]+arr[2])

    for i in range(3, n):
        dp[i] = max(dp[i-2]+arr[i], dp[i-3]+arr[i]+arr[i-1])

    print(dp[n-1])