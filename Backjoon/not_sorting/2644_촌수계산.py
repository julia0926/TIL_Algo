# https://www.acmicpc.net/problem/2644

#입력부 
from collections import deque
n = int(input()) #전체 사람 수 
start, end = map(int, input().split()) #촌수 계산해야 하는 두사람 번호 
m = int(input())  
graph = [[] for _ in range(n+1)]
visited = [-1 for _ in range(n+1)] #-1 방문안함, 0 방문 

def bfs(now):
    dq = deque()
    dq.append(now)
    while dq:
        x = dq.popleft()
        for i in graph[x]: #인접한 값이 있을 때까지
            if visited[i] == -1:
                visited[i] = visited[x] + 1
                dq.append(i)


for i in range(m):
    a, b = map(int, input().split()) #부모, 자식들 간의 관계, 무방향이므로 둘 다 연결
    graph[a].append(b)
    graph[b].append(a)

visited[start] = 0
bfs(start)
print(visited[end])
    
