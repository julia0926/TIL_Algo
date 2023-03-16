#https://school.programmers.co.kr/learn/courses/30/lessons/159994?language=python3
from collections import deque

def solution(cards1, cards2, goal):
    dq1, dq2 = deque(cards1), deque(cards2)
    for word in goal:
        print(word)
        if dq1 and dq1[0] == word:
            dq1.popleft()
        elif dq2 and dq2[0] == word:
            dq2.popleft()
        else:
            if not dq1 or not dq2:
                return "No"

    return "Yes"


print(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]))