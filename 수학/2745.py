# 브론즈 2 - 진법 변환 : https://www.acmicpc.net/problem/2745
n, b = input().split()

piv = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

arr = n[::-1]
result = 0

for idx, val in enumerate(arr):
    result += piv.index(val) * (pow(int(b), idx))

print(result)


