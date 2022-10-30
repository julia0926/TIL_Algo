'''
k : 공통으로 나타나는 정수
두수의 짝궁 : 가장 큰 정수
'''
#https://school.programmers.co.kr/learn/courses/30/lessons/131128
from collections import Counter

def solution(X, Y):
    cx, cy = Counter(X), Counter(Y)
    k = ''.join(sorted(list((cx & cy).elements()), reverse=True))
    if not k: return "-1"
    # elif int(k) == 0: return "0" #아 형변환이 시간을 많이 잡아먹는다!!!
    elif "0" in set(k) and len(set(k)) == 1: return "0"
    else: return k



print(solution("100", "203045"))
print(solution("5525", "1255"))
# solution("12321", "42531")