C,R = map(int,input().split())

my_seat = int(input())
if my_seat > R*C:
    print(0)
    exit()

board = [[0]*C for _ in range(R)]
dir_x = [0,1,0,-1]
dir_y = [-1, 0, 1, 0]
direction = x = y = 0

for i in range(1, C*R+1):

    if i == my_seat:
        print(y+1, x+1)
        break
    else:
        board[x][y] = i #값을 넣는다.
        x += dir_x[direction]
        y += dir_y[direction]

        #범위 벗어났거나 접근하지 않았다면
        if x<0 or y<0 or x>=R or y>=C or board[x][y] != 0:
            x -= dir_x[direction]
            y -= dir_y[direction]
            direction = (direction+1)%4
            x += dir_x[direction]
            y += dir_y[direction]
            

    # print(x, y, board[x][y], "dir", direction)

# for i in range(R):
#     print(board[i])
