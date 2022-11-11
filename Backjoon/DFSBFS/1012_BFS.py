#L2) 유기농 배추 : https://www.acmicpc.net/problem/1012

from collections import deque

t = int(input()) #테스트 케이스 
direction = [[0,1], [0,-1], [1,0], [-1,0]]

def bfs(ground, m, n): #가로, 세로, 카운팅 
    dq = deque()
    dq.append((m,n))
    ground[m][n] = 0
    #print(dq)
    global cnt
    while dq:
        x, y = dq.popleft()
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            if 0<=nx<N and 0<=ny<M and ground[nx][ny] == 1: #범위 안에 있고 배추라면
                dq.append([nx, ny])
                ground[nx][ny] += 1
    cnt += 1 #한 영역 거치면 +1

#입력부 
for i in range(t):
    M, N, K = map(int, input().split())
    ground = [[0] * M for _ in range(N)]
    for j in range(K):
        x, y = map(int, input().split())
        ground[y][x] = 1
    cnt = 0
    for k in range(N): #가로
        for l in range(M): #세로 
            if ground[k][l] == 1:
                bfs(ground, k, l)
    print(cnt)
    

    

