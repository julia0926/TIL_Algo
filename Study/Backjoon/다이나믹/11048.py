n, m = map(int, input().split())
miro = list(list(map(int, input().split())) for _ in range(n))

#왼쪾, 위에, 대각선
for r in range(0, n):
    for c in range(0, m):
        if r == 0 and c == 0:
            continue
        elif r == 0: #맨 위줄
            miro[r][c] += miro[r][c-1] #왼쪽 
        elif c == 0: #맨 왼쪽 
            miro[r][c] += miro[r-1][c]#위쪽
        else:
            miro[r][c] += max(miro[r-1][c], miro[r][c-1], miro[r-1][c-1])

print(miro[n-1][m-1])