#진수 구하기
def change_jinsu(n, q):
    result = ''
    while n:
        n, mod = divmod(n, q)
        result += str(mod)
    return result[::-1]

#소수구하기
def check_sosu(n):
    if n == 1: return False
    for i in range(2, int(n**0.5)+1):
        if n % i ==0: return False
    return True

def solution(n, k):
    value = change_jinsu(n, k)
    result = 0
    for n in value.split('0'):
        if n == "": continue
        if check_sosu(int(n)): 
            result += 1
    return result