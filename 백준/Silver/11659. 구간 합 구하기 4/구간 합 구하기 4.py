import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
cost = [0] * (n+1)

for i in range(n):
    cost[i] = cost[i-1]+arr[i]

for i in range(m):
    a, b = map(int, input().split())
    ans = cost[b-1]-cost[a-2]
    print(ans)