n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
result = []

def dfs():
    if len(result) == m:
        print(*result)
        return
    for i in arr:
        if i not in result:
            result.append(i)
            dfs()
            result.pop()

dfs()
