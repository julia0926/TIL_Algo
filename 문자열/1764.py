# 실버5 : 듣보잡 https://www.acmicpc.net/problem/1764
n, m = map(int, input().split())
no_see = set()
for _ in range(n):
    no_see.add(input())
no_heard = set()
for _ in range(m):
    no_heard.add(input())
result = list(no_heard & no_see)
print(len(result))
for i in sorted(result):
    print(i)
