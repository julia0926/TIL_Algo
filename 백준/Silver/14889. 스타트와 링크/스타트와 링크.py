

n = int(input())
arr = list(list(map(int, input().split())) for _ in range(n)) 
#2차시도 : 약간 참고해서 visited 배열을 써보자
visited = [False] * n
result = []

def dfs(idx, depth):
    global result
    if depth == n//2:
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start += arr[i][j]
                elif not visited[i] and not visited[j]:
                    link += arr[i][j]
        result.append(abs(start-link))
        return

    for i in range(idx, n):
        visited[i] = True
        dfs(i+1, depth+1)
        visited[i] = False

dfs(0 ,0)
print(min(result))