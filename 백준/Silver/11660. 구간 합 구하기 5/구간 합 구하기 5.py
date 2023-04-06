import sys
input = sys.stdin.readline

n, m = map(int,input().split())
arr =[]
for _ in range(n):
    arr.append(list(map(int,input().split())))
prefix_sum = list([0] * (n+1) for _ in range(n+1))

#누적합 구하기
for i in range(1, n+1):
    for j in range(1, n+1):
        prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1] + arr[i-1][j-1]

#계산하기
for _ in range(m):
    x1, y1, x2, y2 = map(int,input().split())
    print(prefix_sum[x2][y2]-prefix_sum[x2][y1-1]-prefix_sum[x1-1][y2]+prefix_sum[x1-1][y1-1])