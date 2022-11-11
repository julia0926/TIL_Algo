from collections import deque
def solution(numbers, target):
    answer = 0
    dq = deque([(0,0)]) #총 합, 깊이
    while dq:
        sum_val, depth = dq.popleft()
       #print(s)
        if depth == len(numbers):
            if sum_val == target:
                answer += 1
        else:
            dq.append((sum_val+numbers[depth], depth+1))
            dq.append((sum_val-numbers[depth], depth+1))
            
    return answer


print(solution([1, 1, 1, 1, 1], 3))