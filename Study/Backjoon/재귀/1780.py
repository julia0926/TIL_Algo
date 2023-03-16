# 실버 2: 종이의 개수  https://www.acmicpc.net/problem/1780
n = int(input())
paper = list(list(map(int, input().split())) for _ in range(n))
result = []

def solution(x, y, size):
    value = paper[x][y]

    for i in range(x, x+size):
        for j in range(y, y+size):
            if value != paper[i][j]:
                #종이 9개로 자름 
                for k in range(3):
                    for l in range(3):
                        solution(x+k*size//3, y+l*size//3, size//3)
                return
    if value == 0:
        result.append(0)
    elif value == -1:
        result.append(-1)
    else:
        result.append(1)

solution(0, 0, n)
print(result.count(-1))
print(result.count(0))
print(result.count(1))


