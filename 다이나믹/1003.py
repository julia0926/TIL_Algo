#L3: 피보나치 함수 https://www.acmicpc.net/problem/1003
T = int(input())
zero = [1, 0, 1]
one = [0, 1, 1]

def fibo(n):
    l = len(zero)
    if n >= l:
        for i in range(l, n+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print(zero[n], one[n])

for i in range(T):
    fibo(int(input()))




# def fibo(n):
#     global zero, one
#     if n == 0: 
#         zero += 1
#         return 0
#     elif n == 1: 
#         one += 1
#         return 1
#     else: return fibo(n-1) +fibo(n-2)


# for i in range(T):
#     n = int(input())
#     zero = 0
#     one = 0 
#     fibo(n)
#     print(f'{zero} {one}')
    
    


