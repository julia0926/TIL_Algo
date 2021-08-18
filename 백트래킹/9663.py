N = int(input())
board = [0 for _ in range(N)] #체스판
count = 0 #퀸 N개를 서로 공격할 수 없게 놓는 경우의 수

#다음행만 가능 -> 중복 제거를 위해 
#인덱스 행, board[x]은 열

def nqueen(x):
    global count
    if N == x: #체스를 끝 행까지 도달했을 때
        count += 1
    else:
        for i in range(N):
            board[x] = i #x번째 행, i열에 퀸 놓음 
            if check(x): #행,열,대각선이 같은 위치에 없다면 
                nqueen(x+1) # 해당 경우보다 한단계 깊이 재귀적으로 또 확인 

def check(val):
    for i in range(val): #열, 대각선 같은지 비교 
        if board[val] == board[i] or abs(board[val] - board[i]) == val - i:
            return False
    return True

nqueen(0)
print(count)