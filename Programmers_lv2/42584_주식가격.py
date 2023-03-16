#https://school.programmers.co.kr/learn/courses/30/lessons/42584

from collections import deque
def solution(prices):
    dq = deque(prices)
    answer = []
    while dq:
        price = dq.popleft()
        sec = 0
        for q in dq:
            sec += 1
            if price > q:
                break
        answer.append(sec)
    print(answer)
print(solution([1, 2, 3, 2, 3]))