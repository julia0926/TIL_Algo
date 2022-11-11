# 실버2 - 연속합 : https://www.acmicpc.net/problem/1912

from re import A


N = int(input())
a = list(map(int, input().split()))
sum_list = [a[0]]
for i in range(N-1):
    sum_list.append(max(sum_list[i], a[i]+a[i+1]))
    print(sum_list)