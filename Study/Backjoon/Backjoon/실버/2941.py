# 실버 5 크로아티아 알파벳 : https://www.acmicpc.net/problem/2941
croa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=', ]
alpha = input()
cnt = 0

for i in croa:
    alpha = alpha.replace(i, '*')

print(len(alpha))