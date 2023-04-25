from collections import deque
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0

def bfs(start):
    visited = [False] * (n+1)
    arr = [0] * (n+1)
    dq = deque()
    dq.append(start)

    while dq:
        v = dq.popleft()
        for a in graph[v]:
            if not visited[a] and a != start:
                arr[a] = arr[v] + 1
                visited[a] = True
                dq.append(a)
    return sum(arr)

result = []
for i in range(1, n+1):
    result.append(bfs(i))

print(result.index(min(result))+1)