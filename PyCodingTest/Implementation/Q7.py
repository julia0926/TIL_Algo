# 백준 18406 : https://www.acmicpc.net/problem/18406

n = input()
mid = len(n) // 2
sum_a = 0
sum_b = 0

for i in range(mid):
    sum_a += int(n[i])
    sum_b += int(n[-(i+1)])

print("LUCKY") if sum_a == sum_b else print("READY")
