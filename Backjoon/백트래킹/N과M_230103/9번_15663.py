n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
result = []
visited = [False] * n

def dfs():
    #base condition
    if len(result) == m:
        print(*result)
        return
    before = 0 #이전 값과 동일하면 안됨!
    for i in range(n):
        if not visited[i] and before != arr[i]:
            visited[i] = True #방문처리하고
            result.append(arr[i]) #값에도 넣는다.
            before = arr[i]
            dfs()
            visited[i] = False
            result.pop()

dfs()