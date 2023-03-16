n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
result = []

def dfs(v):
    #base condition
    if len(result) == m:
        print(*result)
        return
    before = 0
    for i in range(v, n):
        if before != arr[i]:
            result.append(arr[i])
            before = arr[i]
            dfs(i+1)
            result.pop()


dfs(0)