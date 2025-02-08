from collections import deque

def solution(cards1, cards2, goal):
    c1, c2 = deque(cards1), deque(cards2)
    answer = 'Yes'
    for g in goal:
        if c1 and c1[0] == g:
            c1.popleft()
        elif c2 and c2[0] == g:
            c2.popleft()
        else:
            answer = 'No'
    
    return answer