n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

for k in range(n): #거쳐가는 노드
    for i in range(n):
        for j in range(n):
             #그냥 가는 값 있거나 거쳐갈 수 있으면 
            if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1):
                graph[i][j] = 1

for i in range(n):
    print(*graph[i])