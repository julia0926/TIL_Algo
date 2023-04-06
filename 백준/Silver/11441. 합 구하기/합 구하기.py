import sys
input = sys.stdin.readline

n = int(input())
cost = list(map(int, input().split()))

sum_val = [0] * (n+1)
sum_val[1] = cost[0]
for i in range(2, n+1):
    sum_val[i] = cost[i-1] + sum_val[i-1]



m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(sum_val[b]-sum_val[a-1])