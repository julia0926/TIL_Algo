n = int(input())
d = [0] * (n+1)

for i in range(2, n+1):
    d[i] = d[i-1] + 1 #1을 뺴고 시작
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    print(d)

#이거 직접 손으로 해보기  !! 