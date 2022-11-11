#실버5 : 1427 - https://www.acmicpc.net/problem/1427
N = int(input())

arr = sorted(list(str(N)), reverse=True)
for i in arr:
    print(i, end='')