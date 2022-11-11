#L2) 유기농 배추 : https://www.acmicpc.net/problem/1012
import sys 
sys.setrecursionlimit(10000)

from collections import deque

t = int(input()) #테스트 케이스 
direction = [[0,1], [0,-1], [1,0], [-1,0]]

def dfs(m, n): #가로, 세로, 카운팅 
    ground[m][n] = 0 #방문처리 
    for dx, dy in direction:
        nx = m + dx
        ny = n + dy
        if 0<=nx<N and 0<=ny<M and ground[nx][ny] == 1:
            ground[nx][ny] = 0 #방문처리
            dfs(nx, ny)


#입력부 
for i in range(t):
    M, N, K = map(int, input().split()) #가로, 세로 
    ground = [[0] * M for _ in range(N)]
    for j in range(K):
        x, y = map(int, input().split())
        ground[y][x] = 1
    cnt = 0
    for k in range(N): #가로
        for l in range(M): #세로 
            if ground[k][l] == 1:
                dfs(k, l)
                cnt += 1
    print(cnt)
    

    

