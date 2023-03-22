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
    if count == 0:
        return True
    else:
        return False