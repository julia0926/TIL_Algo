INF = int(1e9)

n, m = int(input()), int(input()) #노드, 간선
graph = [[INF] * (n+1) for _ in range(n+1)] #노드 수만큼 갱신

#자기 자신 비용 0 처리
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

#거리 비용 저장
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

#플로이드 워샬 알고리즘 n^3 시간비용
for k in range(1, n+1): #거쳐갈 노드 설정
    for i in range(1, n+1): 
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j]) #i->j vs i->k->j 비교해서 더 작은값


for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print("INFINITY", end=' ')
        else:
            print(graph[i][j], end= ' ')
    print()

