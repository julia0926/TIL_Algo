#https://www.acmicpc.net/problem/7576
from collections import deque

m, n = map(int, input().split()) #가로, 세로
tomato = []
dq = deque()

#시작점을 먼저 queue에 넣음
for y in range(n):
    tomato.append(list(map(int, input().split())))
    for x in range(m):
        if tomato[y][x] == 1:
            dq.append((y, x))

def bfs():
    while dq:
        y, x = dq.popleft()
        for a, b in [[-1, 0],[1,0],[0,-1],[0,1]]:
            ny = a + y
            nx = b + x
            if 0<=ny<n and 0<=nx<m and tomato[ny][nx] == 0:
                dq.append((ny,nx))
                tomato[ny][nx] = tomato[y][x] + 1

bfs()
answer = 0
for i in tomato:
    for val in i:
        if val == 0: #하나라도 0이면 모두 익지못했음
            print(-1)
            exit(0)
    answer = max(answer, max(i))
print(answer-1) #총 며칠이냐이므로 1->2 될때 day1임 

