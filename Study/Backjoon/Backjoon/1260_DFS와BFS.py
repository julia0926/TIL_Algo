# 실버2: DFS와BFS https://www.acmicpc.net/problem/1260

from collections import deque


n, m, v = map(int, input().split())
visited = [False] * (n + 1)
graph = [[0] * (n+1) for _ in range(n+1)]

#양방향 연결 
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

def dfs(v):
    visited[v] = True
    print(v, end=' ')

    for i in range(1, n+1):
        if not visited[i] and graph[v][i] == 1:
            dfs(i)
        
def bfs(v):
    dq = deque([v])
    visited[v] = True

    while dq:
        v = dq.popleft()
        print(v, end=' ')
        for i in range(1, n+1):
            if not visited[i] and graph[v][i] == 1:
                dq.append(i)
                visited[i] = True

dfs(v)
print()
visited = [False] * (n + 1)
bfs(v)