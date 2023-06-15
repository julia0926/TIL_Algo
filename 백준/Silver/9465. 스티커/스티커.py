import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(list(map(int, input().rstrip().split())) for _ in range(2))
    
    for i in range(1, n):
        if i == 1:
            arr[0][i] += arr[1][i-1] #오른쪽 아래
            arr[1][i] += arr[0][i-1] #왼쪽 아래
        else: #위or아래의 왼쪽,왼왼쪽
            arr[0][i] += max(arr[1][i-1], arr[1][i-2])
            arr[1][i] += max(arr[0][i-1], arr[0][i-2]) 
    print(max(arr[0][n-1], arr[1][n-1]))
