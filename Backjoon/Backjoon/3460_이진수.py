#브론즈 3 이진수 : https://www.acmicpc.net/problem/3460

t = int(input())
nlist = list(int(input()) for _ in range(t))

for n in nlist:
    binary = format(n, 'b') #2진수로 변환하는 코드 
    for i in range(len(binary)):
        if binary[-i-1] == '1':
            print(i, end=' ')


