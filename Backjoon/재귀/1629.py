#https://www.acmicpc.net/problem/1629
a, b, c = map(int, input().split())

def fpow(a, b):
    if b == 1:
        return a % c
    tmp = fpow(a, b//2)
    if b % 2 == 0:
        print(f'{tmp}*{tmp}%{c}={tmp * tmp % c}')
        return tmp * tmp % c
    else:
        print(f'{tmp}*{tmp}*{a}%{c}={tmp * tmp * a % c}')
        return tmp * tmp * a % c
    

print(fpow(a,b))