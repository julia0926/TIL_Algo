#실버2: 연결 요소의 개수 https://www.acmicpc.net/problem/11724
import sys
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False for _ in range(n+1)]
cnt = 0

def dfs(value):
    visited[value] = True
    for i in graph[value]:
        if not visited[i]:
            dfs(i)

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        cnt += 1


print(cnt)