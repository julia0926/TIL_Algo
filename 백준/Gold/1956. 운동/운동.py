v, e = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (v) for _ in range(v)]

for i in range(v):
    for j in range(v):
        if i == j:
            graph[i][j] = 0

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = c

for k in range(v):
    for i in range(v):
        for j in range(v):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

result = INF
for i in range(v):
    for j in range(v):
        if i != j:
            result = min(result, graph[i][j]+graph[j][i])
if result == INF:
    print(-1)
else:
    print(result)