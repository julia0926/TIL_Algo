t = int(input())
case = [int(input()) for _ in range(t)]
d = [0] * 100

d[1] = 1
d[2] = 2
d[3] = 4

for i in case:
    for j in range(4, i+1):
        d[j] = d[j-1]+d[j-2]+d[j-3]
    print(d[i])