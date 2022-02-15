#볼링공 고르기
#답은 맞는데, 풀이가 달라서 맞는지 모르게씀..
n, m = map(int, input().split())
boling = list(map(int, input().split()))
cnt = 0

for i in range(n):
    for j in range(i, n):
        if boling[i] == boling[j]:
            continue
        cnt += 1

print(cnt)