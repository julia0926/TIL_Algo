#https://www.acmicpc.net/problem/1051
n, m = map(int, input().split())
if n == 1 or m == 1:
    print(1)
else:
    arr = [list(map(int, input())) for _ in range(n)]


    check = min(n, m)
    result = 0

    for i in range(n):
        for j in range(m):
            for k in range(check):
                if (i + k) < n and (j + k) < m and arr[i][j] == arr[i+k][j] == arr[i][j+k] == arr[i+k][j+k]:
                    result = max(result, (k+1)*(k+1))

    print(result)