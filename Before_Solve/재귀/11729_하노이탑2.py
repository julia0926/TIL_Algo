# 실버1 하노이탑 이동 순서 : https://www.acmicpc.net/problem/11729
n = int(input())
result = []

def hanoi(n, now, by, to):
    if n == 1:
        result.append([now, to])
        return
    hanoi(n-1, now, to, by)
    result.append([now, to])
    hanoi(n-1, by, now, to)

hanoi(n, 1, 2, 3)
print(len(result))
for i in result:
    print(i[0], i[1])