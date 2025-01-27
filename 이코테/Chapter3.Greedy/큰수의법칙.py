from collections import deque

n = int(input()) #컴퓨터의 수
m = int(input()) #컴퓨터의 쌍
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(val):
    dq = deque()
    dq.append(val)
    visited[val] = True
    count = 0

    while dq:
        pop_val = dq.popleft()
        for k in graph[pop_val]:
            if not visited[k]:
                visited[k] = True
                count += 1
                dq.append(k)
    return count

print(bfs(1))