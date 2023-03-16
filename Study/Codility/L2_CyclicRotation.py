# https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/

from collections import deque
def solution(A, K):
    if len(A) == K:
        return A
    elif A == []:
        return 
    else:
        dq = deque(A)
        for _ in range(K):
            dq.appendleft(dq.pop())
    return list(dq)

print(solution([3, 8, 9, 7, 6], 3))
print(solution([0, 0, 0], 1))