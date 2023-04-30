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