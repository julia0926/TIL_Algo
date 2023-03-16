# https://www.acmicpc.net/problem/2628
from re import T


x, y = map(int, input().split())
row = [0, x]
col = [0, y]

num = int(input())

for _ in range(num):
    gubun, value = map(int, input().split())
    if gubun == 1:
        row.append(value)
    else:
        col.append(value)

row.sort(reverse=True)
col.sort(reverse=True)
result_row, result_col = [], []

for i in range(len(row)-1):
    result_row.append(row[i] - row[i+1])

for i in range(len(col)-1):
    result_col.append(col[i] - col[i+1])

print(max(result_col) * max(result_row))