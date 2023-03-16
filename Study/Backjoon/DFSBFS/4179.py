#https://www.acmicpc.net/problem/4179
# 내일 다시도전.. 이해가 안감 

from collections import deque
R, C = map(int, input().split()) #행, 열
miro = []
fire = deque()
jihun = deque()
fire_dist = [[0] * C for _ in range(R)]
jihun_dist = [[0] * C for _ in range(R)]
dist = [[-1, 0], [1,0], [0, -1], [0, 1]]
# print(fire_dist, jihun_dist)

#입력 / 불과 지훈 위치 저장 
for i in range(R):
    miro.append(list(input()))
    for j in range(C):
        if miro[i][j] == 'J':
            jihun.append((i, j))
            jihun_dist[i][j] = 1
        elif miro[i][j] == 'F':
            fire.append((i, j))
            fire_dist[i][j] = 1

def fire_bfs():
    while fire:
        dy, dx = fire.popleft()
        for a, b in dist:
            ny = dy + a
            nx = dx + b
            if 0<=ny<R and 0<=nx<C and miro[ny][nx] != '#' and fire_dist[ny][nx] == 0: #지나갈 수 있고, 
                fire.append((ny, nx))
                fire_dist[ny][nx] = fire_dist[dy][dx] + 1

fire_bfs()
print(fire_dist)

def jihun_bfs():
    while jihun:
        dy, dx = jihun.popleft()
        for a, b in dist:
            ny = a + dy
            nx = b + dx
            #범위를 벗어나면 종료이므로
            if not (0<=ny<R and 0<=nx<C):
                print(jihun_dist[ny][nx])
                continue
            if jihun_dist[ny][nx] >= 0 or miro[ny][nx] == '#':
                continue
            #자신이 도착한 시간과 동시에 불이 도착하거나, 혹은 자신보다 더 빨리 불이 도착하는 자리로는 갈 수 없기 때문에
            if fire_dist[ny][nx] != 0 and fire_dist[ny][nx] <= jihun_dist[ny][nx] + 1:
                continue
            jihun.append((ny, nx))
            jihun_dist[ny][nx] = jihun_dist[dy][dx] + 1

print(jihun_dist)

'''
불의 bfs, 지훈이 bfs 따로 돌리자 
'''
# def bfs():
#     while fire:
#         y, x = fire.popleft() #J의 위치
        

        
