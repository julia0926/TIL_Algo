n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
result = []

def dfs(v):
    #base condition
    if len(result) == m:
        print(*result)
        return
    before = 0
    for i in range(n):
        if before != arr[i] and v <= arr[i]:
            result.append(arr[i])
            before = arr[i]
            dfs(arr[i])
            result.pop()

dfs(0)

#더 작은 값은 안된다!!
