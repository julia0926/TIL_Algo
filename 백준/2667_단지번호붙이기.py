#bfs 연습 : https://www.acmicpc.net/problem/2667

from collections import deque

dx = [0,0,-1,1]
dy = [1,-1,0,0]
result_count = []

def bfs(a, b):
    global n 
    global house

    dq = deque()
    dq.append((a,b))
    house[a][b] = 0 #방문처리
    house_count = 1

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #범위 내에 잇고, 값이 1이라면 
            if 0 <= nx < n and 0 <= ny < n and house[nx][ny] == 1:
                house[nx][ny] = 0 #방문 처리 해주고
                dq.append((nx,ny)) #큐에 현재 값을 넣어줌 
                house_count += 1
    
    return house_count

# 입력부
n = int(input())
house = []
for i in range(n):
    house.append(list(map(int, input())))

#bfs 순환
for i in range(n):
    for j in range(n):
        if house[i][j] == 1:
            result_count.append(bfs(i, j))

#결과 출력 
result_count.sort()
print(len(result_count))
for i in result_count:
    print(i)