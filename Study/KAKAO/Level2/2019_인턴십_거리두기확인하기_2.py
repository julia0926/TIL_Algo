# https://school.programmers.co.kr/learn/courses/30/lessons/81302
'''
거리두기 지키면 1, 한명이라도 안지키면 0
'''

from collections import deque

def bfs(place):
    #check 
    start = [] #p가 있는 위치 
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P': #응시자가 안은 자리
                start.append([i, j])
    if not start:
        return 1
    ######

    for i, j in start:
        dq = deque()
        dq.append((i, j))
        visited = [[0] * 5 for _ in range(5)]
        visited[i][j] = 1

        while dq:
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]
            x, y = dq.popleft()
            if visited[x][y] == 3:
                continue #거리가 3이라면 체크할 필요 없음 ,, 
            
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if 0<=nx<5 and 0<=ny<5 and not visited[nx][ny]:
                    if place[nx][ny] == 'O': #빈자리는 방문처리 + 큐에넣고 지나감
                        dq.append([nx, ny])
                        visited[nx][ny] = visited[x][y] + 1
                    if place[nx][ny] == 'P': #응시자가 있으면 ?!
                        return 0
    return 1


def solution(places):
    answer = []
    for place in places:
        answer.append(bfs(place))
    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))