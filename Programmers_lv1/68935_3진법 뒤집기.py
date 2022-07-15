# https://school.programmers.co.kr/learn/courses/30/lessons/68935

'''
1) 10 -> 3진법 변환
5를 3으로 나눌 수 있을 때까지 나누면
몫 1 나머지 2 -> 12(몫, 나머지)

'''
def change(n):
    result = ''
    while n:
        n, mod = divmod(n, 3)
        result += str(mod)
    #원래 진법 구하는 거라면 뒤집기 까지 해야함 (근데 문제조건에서 또 뒤집으라해서 아예 안뒤집음)
    #result[::-1]
    return str(result)

def solution(n):
    return int(change(n), 3)

print(solution(125))
