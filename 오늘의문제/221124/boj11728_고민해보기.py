#https://www.acmicpc.net/problem/11728
#흠... 맘에 드는 코드는 아님...

n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
answer = []
adx, bdx = 0, 0

for _ in range(len(a+b)):
    if adx == len(a):
        answer.append(b[bdx])
        bdx += 1
        
    elif bdx == len(b):
        answer.append(a[adx])
        adx += 1
        
    elif a[adx] > b[bdx]:
        answer.append(b[bdx])
        bdx += 1
    else:
        answer.append(a[adx])
        adx += 1
print(*answer)
    