def check(x, y, col):
    for i in range(x):
        if col[i] == y or abs(y-col[i]) == x-i: #같은 줄이면 안되고, (x2-x1) == (y2-y1)이 같으면 대각선이므로
            return False
    return True

def queen(x, n, col):
    if x == n:
        return 1

    count = 0
    for y in range(n):
        if check(x, y, col): #퀸을 놓을 수 있는 조건에 부합한다면, 
            col[x] = y #해당 x,y에 퀸을 놓고 
            count += queen(x+1, n, col) #퀸을 놓을 수 있다면 다음줄도 계산
    return count


def solution(n):
    return queen(0, n,  [0] * n)