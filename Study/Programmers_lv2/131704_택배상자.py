#https://school.programmers.co.kr/learn/courses/30/lessons/131704

from collections import deque

def solution(order):
    packs = deque([i for i in range(1, len(order)+1)])
    container, result = [], []
    for o in order:
        while packs:
            value = packs.popleft()
            if value != o:
                container.append(value)
                
            else: #같으면?
                result.append(value)
    print(result)
    answer = 0
    return answer

solution([4, 3, 1, 2, 5])