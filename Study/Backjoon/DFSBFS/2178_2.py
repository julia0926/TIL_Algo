from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    
def bfs(x, y):
    dq = deque()
    dq.append((x, y))
    
    while dq:
        dx, dy = dq.popleft()
        for a, b in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            nx = a + dx
            ny = b + dy
            if 0<=nx<n and 0<=ny<m and int(graph[nx][ny]) == 1:
                graph[nx][ny] = graph[dx][dy] + 1
                dq.append((nx,ny))

bfs(0, 0)
print(graph[n-1][m-1])