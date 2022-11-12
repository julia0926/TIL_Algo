# https://school.programmers.co.kr/learn/courses/30/lessons/42885

from collections import deque

def solution(people, limit):
    answer = 0
    dq = deque(sorted(people))
    while dq:
        if len(dq) == 1:
            answer += 1
            break
        if dq[0] + dq[-1] <= limit: #같이 탈수있다면
            dq.popleft() 
        dq.pop()
        answer += 1

    return answer