#실버 3 - 동전 0 : https://www.acmicpc.net/problem/11047

n, k = map(int, input().split())
coin = []
for i in range(n):
    coin.append(int(input()))
result = 0
coin.sort(reverse=True)

for i in coin:
    if k // i > 0:
        result += k // i
        k = k % i

print(result)