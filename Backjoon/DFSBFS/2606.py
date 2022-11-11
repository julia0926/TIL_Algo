#실버 3 :바이러스 https://www.acmicpc.net/problem/2606
from collections import deque

V = int(input()) #노드수
E = int(input()) #간선수
graph = [[] for _ in range(V+1)]
visited = [False] * (V+1)
 
#무방향 그래프 연결 
for i in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
cnt = 0
def bfs(v):
    dq = deque([v])
    visited[v] = True
    global cnt
    while dq:
        v = dq.popleft()
        for i in graph[v]:
            if not visited[i]:
                cnt += 1
                dq.append(i)
                visited[i] = True
bfs(1)
print(cnt)