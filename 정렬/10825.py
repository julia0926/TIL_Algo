n = int(input())
quiz = [list(input().split()) for _ in range(n)]

result = sorted(quiz, key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for i in result:
    print(i[0])