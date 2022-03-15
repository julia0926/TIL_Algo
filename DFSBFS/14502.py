#14502 골드 5 연구소 : https://www.acmicpc.net/problem/14502

from collections import deque
import copy
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
house = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
result = 0

def bfs():
    global result
    deep_arr = copy.deepcopy(house)
    dq = deque()
    for i in range(n):
        for j in range(m):
            if deep_arr[i][j] == 2:
                dq.append((i, j))

    while dq:
        a, b = dq.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<m and deep_arr[nx][ny] == 0:
                deep_arr[nx][ny] = 2 #바이러스를 퍼지게 하고
                dq.append((nx, ny))
    virus = 0
    for i in range(n):
        virus += deep_arr[i].count(0)
    result = max(virus, result)


def wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if house[i][j] == 0:
                house[i][j] = 1 #벽을 세우고
                wall(cnt+1)
                house[i][j] = 0

wall(0)
print(result)