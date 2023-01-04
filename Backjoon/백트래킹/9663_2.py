#https://www.acmicpc.net/problem/9663
n = int(input())
row = [False] * n
left_digonal = [False] * 2*n #왼쪽 대각선
right_digonal = [False] * 2*n #오른쪽 대각선
result = 0
#cur = y다 

def solve(cur):
    global result
    if cur == n:
        result += 1
        return
    for i in range(n):
        if row[i] or left_digonal[i+cur] or right_digonal[i-cur+n-1]:
            continue
        row[i], left_digonal[i+cur], right_digonal[i-cur+n-1] = True, True, True
        solve(cur+1)
        row[i], left_digonal[i+cur], right_digonal[i-cur+n-1] = False, False, False

solve(0)
print(result)