#다리를 건너는데 필요한 시간이 bridge_length
from collections import deque


def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    cross = deque([0]*bridge_length) #다리를 건너는 트럭 
    due_time = 0
    while cross:
        due_time += 1
        cross.popleft()
        if truck_weights: #대기 트럭이 있는동안만 
            if sum(cross) + truck_weights[0] <= weight: #10kg까지만 견딜 수 있다면
                cross.append(truck_weights.popleft())
            else:
                cross.append(0)
    print(due_time)

        
    answer = 0
    return answer

solution(2, 10, [7,4,5,6])