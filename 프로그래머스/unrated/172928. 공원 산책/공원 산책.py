
def solution(park, routes):
    x, y = 0, 0
    row, col = len(park),len(park[0])
    move = {"E":(0,1),"W":(0,-1),"S":(1,0),"N":(-1,0)}

    #시작점 찾기
    for i in range(row):
        for j in range(col):
            if park[i][j] == "S":
                x, y = i, j
                break
    print("start", x,y)
    for route in routes:
        r0, r1 = route.split()
        dx, dy = move[r0]
        nx, ny = x, y #신규값을 갱신하기 위해 
        for _ in range(int(r1)):
            if 0<=nx+dx<row and 0<=ny+dy<col and park[nx+dx][ny+dy] != "X":
                nx += dx
                ny += dy
            else: #원상복귀
                nx, ny = x, y
                break
        x, y = nx, ny

    return [x, y]