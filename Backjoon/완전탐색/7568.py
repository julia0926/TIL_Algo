n = int(input())
human = []
for _ in range(n):
    x, y = map(int, input().split())
    human.append([x, y]) #원본 배열 

result = []
for i in range(n):
    rank = 1
    for j in range(n):
        if human[i][0] < human[j][0] and human[i][1] < human[j][1]:
            rank += 1
    result.append(rank)

print(*result)