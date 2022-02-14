import math

def change(n, k):
    s = ''
    while n:
        s += str(n % k) #몫 
        n //= k
    return s[::-1] #문자열 역순으로 출력 

def is_prime(n):
    if n == 1: return False
    k = int(math.sqrt(n))
    for i in range(2, k+1):
        if n % i == 0: return False
        i += 1
    return True

def solution(n, k):
    answer = 0
    s = change(n, k)
    print(s.split('0'))
    for n in s.split('0'):
        if not n: continue
        print(n)
        if is_prime(int(n)): answer += 1
    return answer


print(solution(437674, 3))
# n = 437674
# k = 3