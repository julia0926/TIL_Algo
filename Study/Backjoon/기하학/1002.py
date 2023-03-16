import math


n = int(input())

for i in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    R = math.sqrt((x2-x1) * (x2-x1) + (y2-y1) * (y2-y1))
    if r1 > r2:
        r1, r2 = r2, r1
    cnt = 0
    if R > r2:
        if R > r1 + r2:
            cnt = 0
        elif R == r1 + r2:
            cnt = 1
        else:
            cnt = 2
    elif 0 < R <= r2:
        if r2 > R + r1:
            cnt = 0
        elif r2 == R + r1:
            cnt = 1
        else:
            cnt = 2
    elif R == 0:
        if r1 != r2:
            cnt = 0
        else:
            cnt = -1 #무한대 일 경우
    print(cnt)