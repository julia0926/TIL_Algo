def solution(wallpaper):
    file = []
    row, col = len(wallpaper), len(wallpaper[0])
    lux, luy, rdx, rdy = 0,0,0,0
    for i in range(row):
        for j in range(col):
            if wallpaper[i][j] == "#":
                file.append([i,j])
    # print(file)
    max_v = max(row, col)
    min_x, min_y = max_v, max_v
    max_x, max_y = 0, 0
    for x, y in file:
        max_x = max(x, max_x)
        max_y = max(y, max_y)
        min_x = min(x, min_x)
        min_y = min(y, min_y)
        # print(min_x, min_y)
    rdx, rdy = max_x+1, max_y+1
    answer = [min_x, min_y, rdx, rdy]
    return answer