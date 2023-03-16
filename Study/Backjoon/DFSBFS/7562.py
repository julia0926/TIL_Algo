#https://www.acmicpc.net/problem/7562
from collections import deque
dx = [-1,-1,-2,-2,1,1,2,2]
dy = [2,-2,1,-1,2,-2,1,-1]

case = int(input())

def bfs(x, y):
    dq = deque()
    dq.append((x,y))
    chasepan[x][y] = 1

    while dq:
        a, b = dq.popleft()
        if a == move[0] and b == move[1]:
            return chasepan[a][b] -1
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<l and 0<=ny<l and chasepan[nx][ny] == 0:
                dq.append((nx,ny))
                chasepan[nx][ny] = chasepan[a][b] + 1
                # print("-->", chasepan[nx][ny])

for _ in range(case):
    l = int(input())
    now = list(map(int,input().split()))
    move = list(map(int,input().split()))
                    
    if now == move:
        print(0)
        continue
    chasepan = list([0 for _ in range(l)] for _ in range(l))
    print(bfs(now[0],now[1]))