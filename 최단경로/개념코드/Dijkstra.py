import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) #무한대 

n, m = map(int, input().split()) #노드 개수, 간선 개수
start = int(input()) #시작 노드 번호
graph = [[] for _ in range(n+1)] #각 노드에 연결된 정보를 담는 리스트 
distance = [INF] * (n + 1) #거리 = 노드 + 1

#모든 간선 정보 입력 
for _ in range(m):
    a, b, c = map(int, input().split()) 
    graph[a].append((b, c)) #a번 노드에서 b번 노드로 가는 비용이 c이다.

def dijkstra(start):
    q = []
    #시작 노드로 가기위한 경로는 0, 큐에 삽입 
    heapq.heappush(q, (0, start)) #경로, 시작노드
    distance[start] = 0
     #큐가 비어있지 않다면 
    while q:
        dist, now = heapq.heappop(q) #최단 거리가 짧은 정보 꺼냄
        if distance[now] < dist:
            continue
        #현재 노드와 연결된 다른 인접한 노드들 확인 
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]: #다른 노드로 거쳐서 < 현재노드 
                distance[i[0]] = cost #해당 노드의 거리값을 갱신
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF: #도달할 수 없는 경우
        print("INFINITY")
    else: #도달할 수 있는 경우 
        print(distance[i])


# <입력값 >
# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2