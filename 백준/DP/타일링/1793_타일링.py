#https://www.acmicpc.net/problem/1793


def solution(n):
    if n == 0 or n == 1:
        return 1
    d = [0] * (n+1)
    d[1] = 1
    d[2] = d[1] + 2
    for i in range(3, n+1):
        d[i] = d[i-1] + (2*d[i-2])
    return d[n]

while True:
    try:
        print(solution(int(input())))
    except:
        break
