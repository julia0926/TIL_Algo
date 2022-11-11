# 4번 : https://www.acmicpc.net/problem/15652

n, m = map(int, input().split())
result = []

def dfs(depth, k):
    if depth == m:
        print(*result)
        return
    for i in range(k, n+1):
        result.append(i)
        dfs(depth+1, i)
        result.pop()

dfs(0, 1)