from collections import deque


def solution(pal_list):
    dq = deque(pal_list)
    while dq:
        if dq.popleft() != dq.pop():
            return False
    return True

print(solution([1,2,2,3,1]))