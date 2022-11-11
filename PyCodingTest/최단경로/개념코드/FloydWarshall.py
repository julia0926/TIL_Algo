INF = int(1e9)

n = int(input()) #노드 개수
m = int(input()) #간선 개수

graph = [[INF] * (n + 1) for _ in range(n+1)]

#자기 자신 -> 자기자신 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

#각 간선에 대한 정보를 입력받아 ,그 값으로 초기화
for _ in range(m):
    a, b, c = map(int,input().split())
    graph[a][b] = c

print("-----------------")
#플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

#수행된 결과 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        #도달 못하면 무한대로
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        else:
            print(graph[a][b], end=" ")

    print()

#입력예
# 4
# 7
# 1 2 4
# 1 4 6
# 2 1 3
# 2 3 7
# 3 1 5
# 3 4 4
# 4 3 2