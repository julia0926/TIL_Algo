n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
result = []

def dfs():
    if len(result) == m:
        print(*result)
        return
    for i in range(len(arr)):
        result.append(arr[i])
        dfs()
        result.pop()


           

dfs()
