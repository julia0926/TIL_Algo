#https://school.programmers.co.kr/learn/courses/30/lessons/42583
from collections import deque

def solution(bridge_length, weight, truck_weights):
    #weight 키로 이상이면 pop
    secend = 0
    truck_weights = deque(truck_weights)
    cross = deque([0] * bridge_length) #다리에 있는 트럭 
    print(cross)
    while cross: #다리에 있는동안 
        secend += 1
        cross.popleft()
        print(secend, cross)
        if truck_weights:
            if sum(cross) + truck_weights[0] <= weight:
                cross.append(truck_weights.popleft())
            else:
                cross.append(0)
    return secend


print(solution(2, 10, [7,4,5,6]))