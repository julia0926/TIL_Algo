from collections import defaultdict

n = int(input())
dic = defaultdict(int)
for _ in range(n):
    number, p, q, r = list(map(int, input().split()))
    multi_val = p*q*r
    sum_val = p+q+r
    dic[number] = (multi_val, sum_val)

sorted_dic = sorted(dic.items(), key=lambda x: (x[1][0], x[1][1], x[0]))

for i in range(3):
    print(sorted_dic[i][0], end=' ')
