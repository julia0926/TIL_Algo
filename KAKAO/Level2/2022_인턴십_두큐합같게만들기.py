from collections import deque

def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)
    count = 0
    while True:
        if not q1 or not q2:
            return -1
        if sum(q1) == sum(q2):
            break
        elif sum(q1) < sum(q2):
            q1.append(q2.popleft())
        else:
            q2.append(q1.popleft())
        print(q1, q2, sum(q1), sum(q2))
        count += 1
    
    return count

# solution([3, 2, 7, 2], [4, 6, 5, 1])
# solution([1, 2, 1, 2], 	[1, 10, 1, 2]	)
print(solution([1,1], [1,5]))