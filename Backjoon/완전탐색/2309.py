# 일곱 난쟁이 : https://www.acmicpc.net/problem/2309

from itertools import combinations


member = list(int(input()) for _ in range(9))
member.sort()
sum_meb = list(combinations(member, 7))
for i in sum_meb:
    if sum(i) == 100:
        x = list(i)
        break

for j in x:
    print(j)