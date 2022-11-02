# https://school.programmers.co.kr/learn/courses/30/lessons/120882

from collections import defaultdict

def solution(score):
    ev = []
    for a, b in score:
        ev.append((a+b)/2)
    ev_dic = defaultdict(int)
    for idx, value in enumerate(sorted(ev, reverse=True)):
        if ev_dic[value] == 0:
            ev_dic[value] = idx+1
    result = []
    for e in ev:
        result.append(ev_dic[e])
    return result

    

solution([[80, 70], [90, 50], [40, 70], [50, 80]])
solution([[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]])

