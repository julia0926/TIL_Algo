#https://school.programmers.co.kr/learn/courses/30/lessons/12909
from collections import deque

def solution(s):
    dq = deque(s)
    count = 0
    while dq:
        value = dq.popleft()
        if value == '(':
            count += 1
        else:
            count -= 1

        if count < 0:
            return False
    return True if count == 0 else False
        
print(solution("(())()"))
print(solution(")()("))