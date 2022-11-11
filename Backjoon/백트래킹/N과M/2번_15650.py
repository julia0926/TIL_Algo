# 실버 2 : https://www.acmicpc.net/problem/15650

from itertools import combinations

n, m = map(int, input().split())
result = []

def dfs(v):
    if len(result) == m:
        print(*result)
        return
    for i in range(v, n+1):
        result.append(i)
        dfs(i+1)
        result.pop()

dfs(1)

# 내장된 combinations 사용
# for x in combinations(range(1, n+1), m):
#     print(' '.join(map(str, x)))

# arr = list(combinations(range(1, n+1), m))
# for i in arr:
#     print(*i)