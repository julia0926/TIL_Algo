from collections import deque

#불을 먼저 퍼트린다.
def fire_move():
    while fire_dq:
        x, y = fire_dq.popleft()
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            if not (0<=nx<r and 0<=ny<c):
                continue
            if graph[nx][ny] == '#' or fire[nx][ny]:
                continue
            fire[nx][ny] = fire[x][y] + 1
            fire_dq.append((nx,ny))

def jihun_move():
    while jihun_dq:
        x, y = jihun_dq.popleft()
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            if not (0<=nx<r and 0<=ny<c): #범위를 벗어나면 탈출이므로 프린트 후 종료
                print(jihun[x][y])
                # print(graph)
                return
            if graph[nx][ny] == '#' or jihun[nx][ny]:
                continue
            if fire[nx][ny] and jihun[x][y] + 1 >= fire[nx][ny]: #불이 이미 퍼지고, 
               continue
            jihun[nx][ny] = jihun[x][y] + 1
            jihun_dq.append((nx, ny)) 
    #탈출하지 못했으면
    print("IMPOSSIBLE")

r, c = map(int, input().split())
graph = []
fire_dq = deque()
jihun_dq = deque()

jihun = [[0] * c for _ in range(r)]
fire = [[0] * c for _ in range(r)]

direction = [(0,1),(0,-1),(1,0),(-1,0)]

for i in range(r):
    gh = list(input())
    graph.append(gh)
    for j in range(c):
        if gh[j] == 'J':
            jihun_dq.append((i, j))
            jihun[i][j] = 1
        elif gh[j] == 'F':
            fire_dq.append((i,j))
            fire[i][j] = 1
fire_move()
jihun_move()