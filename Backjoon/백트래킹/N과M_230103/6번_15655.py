n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
result = []

def dfs(v):
    if len(result) == m:
        print(*result)
        return
    for i in range(v, len(arr)):
        result.append(arr[i])
        dfs(i+1)
        result.pop()


           

dfs(0)
