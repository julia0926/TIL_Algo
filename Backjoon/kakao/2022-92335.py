# Lv2. k진수에서 소수 개수 구하기 : https://programmers.co.kr/learn/courses/30/lessons/92335

def solution(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1]

