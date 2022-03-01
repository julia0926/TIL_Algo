# 실버 2: 하노이탑 https://www.acmicpc.net/problem/1914

n = int(input())
onepan = [i for i in range(3)]
result = []
def hanoi(num, now, by, to):
    if num == 1:
        result.append((now, to))
        return
    hanoi(num-1, now, to, by)
    result.append((now, to))
    hanoi(num-1, by, now, to)

if n <= 20: 
    hanoi(n, 1, 2, 3)
    print(len(result))
    for i in result:
        print(i[0], i[1])
else:
    print(pow(2, n)-1)

