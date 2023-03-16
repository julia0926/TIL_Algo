'''
거리두기 지키면 -> 1
안지키면 -> 0
'''

from collections import deque

def bfs(place):
    start = []
    #시작점의 위치(P가 있는)를 start 배열에 넣음
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                start.append([i, j])
    
    for s in start:
        dq = deque([s])
        visited = [[False] * 5 for _ in range(5)]
        distance = [[0] * 5 for _ in range(5)]
        dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
        
        #맨 처음 값은 방문처리 
        x, y = s[0], s[1]
        visited[x][y] = True
        
        while dq:
            y, x = dq.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                #범위 내에 있고 방문한적이 없어야 한다..
                if 0<=nx<5 and 0<=ny<5 and not visited[ny][nx]:
                    # O를 만났을 때
                    if place[ny][nx] == 'O':
                        dq.append([ny, nx])
                        distance[ny][nx] = distance[y][x] + 1
                        visited[ny][nx] = True

                    # P를 만났는데 거리두기가 지켜지지 않으면   => 탐색 종료
                    elif place[ny][nx] == 'P' and distance[ny][nx] <= 1:
                        return 0
    return 1

def solution(places):
    answer = []

    for place in places:
        answer.append(bfs(place))
    return answer



print(solution([
    ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))