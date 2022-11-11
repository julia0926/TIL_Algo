from collections import deque


N, M = map(int, input().split()) #세로 , 가로 
arr = []
direction = [[0,1], [0,-1], [1,0], [-1,0]]
for _ in range(N):
    arr.append(list(map(int, input())))
#큐 자체가 최소힙 기반이기 떄문에 .. 
def bfs(x, y):
    dq = deque()
    dq.append((x, y))
    while dq:
        a, b = dq.popleft()
        #print(a, b)
        for dx, dy in direction:
            nx = a + dx 
            ny = b + dy
            if 0<=nx<N and 0<=ny<M and arr[nx][ny] == 1:
                dq.append([nx, ny])
                arr[nx][ny] = arr[a][b] + 1
                print(arr[nx][ny])
    return arr[N-1][M-1]
print(bfs(0, 0))
                

