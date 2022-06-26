#더하기 사이클 : https://www.acmicpc.net/problem/1110

N = int(input())
n = N
cnt = 0
while True:
    new = n // 10 + n % 10
    new = (n % 10) * 10 + new % 10
    cnt += 1
    if N == new:
        print(cnt)
        break
    else:
        n = new

