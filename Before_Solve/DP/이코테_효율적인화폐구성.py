n, m = map(int, input().split()) #N가지 코인, 최종 M원
coins = [int(input()) for _ in range(n)] #N가지 코인들의 종류

d = [10001] * (m+1)
d[0] = 0 #0원으로는 0개 만들 수 있으므로 초기화 

for i in range(n):
    for j in range(coins[i], m+1):
        if d[j-coins[i]] != 10001: #계산 한적이 없다면
            d[j] = min(d[j], d[j-coins[i]]+1)
            print(j, d[j])

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
