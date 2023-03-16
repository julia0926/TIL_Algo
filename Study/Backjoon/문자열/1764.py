# 실버5 : 듣보잡 https://www.acmicpc.net/problem/1764
n, m = map(int, input().split())
see, heard= set(), set()
for i in range(n):
    see.add(input())
for j in range(m):
    heard.add(input())
result = sorted(list(see&heard))
print(len(result))
for r in result:
    print(r)