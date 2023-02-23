'''
https://school.programmers.co.kr/learn/courses/30/lessons/154540
최대 며칠씩 머물 수 있는지 
x = 바다
숫자 = 무인도
모든 숫자를 합한 값은 며칠 머무는지..
'''

from collections import deque


direction = [[0,1], [1,0], [0, -1], [-1,0]]
def solution(maps):
    result = []
    row, col = len(maps), len(maps[0])

    maps = [list(maps[i]) for i in range(row)]
    
    def bfs(x, y):
        count = int(maps[x][y])
        dq = deque([[x,y]])
        maps[x][y] = 'X' #방문처리

        while dq:                                                                                   
            x, y = dq.popleft()
            for dx, dy in direction:
                nx = dx + x
                ny = dy + y
                if 0<=nx<row and 0<=ny<col and maps[nx][ny] != 'X':
                    dq.append([nx,ny])
                    count += int(maps[nx][ny])
                    maps[nx][ny] = 'X'
        
        return count

    for i in range(row):
        for j in range(col):
            if maps[i][j] != 'X':
                result.append(bfs(i,j))
    if not result:
        return [-1]
    else:
        return sorted(result)
solution(["X591X","X1X5X","X231X", "1XXX1"])
print(solution(["XXX","XXX","XXX"]))