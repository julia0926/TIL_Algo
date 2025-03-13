n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(input())
    
answer = []
for i in range(n-7):
    for j in range(m-7): #체스판 자르기 
        black_c, white_c = 0, 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0: #짝수번째라면 
                    if board[k][l] == 'B': black_c += 1
                    else: white_c += 1
                else: #홀수 번째라면
                    if board[k][l] == 'W': black_c += 1
                    else: white_c += 1
        answer.append(black_c)
        answer.append(white_c)

print(min(answer))