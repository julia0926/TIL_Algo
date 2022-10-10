#https://school.programmers.co.kr/learn/courses/30/lessons/120871
from collections import defaultdict

def solution(n):
    dic = defaultdict(int)
    i = 1
    idx = 1
    while idx <= n:
        if i % 3 == 0 or '3' in str(i): #3이 포함되있으면
            i += 1
        else:
            dic[idx] = i
            idx += 1
            i += 1

    return dic[n]

solution(40)

#딕셔너리 안저장하고 바로 그냥 for문으로 값 구하면 메모리 조금 절약할듯
def solution2(n):
    answer, num = 0, 0
    for i in range(1, n+1):
        num += 1
        while num % 3 == 0 or '3' in str(num):
            num += 1
    answer = num
    return answer