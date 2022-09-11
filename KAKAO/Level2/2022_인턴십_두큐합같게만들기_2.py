from collections import deque


def solution(queue1, queue2):
    dq1, dq2 = deque(queue1), deque(queue2)
    sum_q1, sum_q2 = sum(queue1), sum(queue2)
    answer = 0

    while sum_q1 != sum_q2:
        if not dq1 or not dq2:
            return -1
        if sum_q1 < sum_q2:
            sum_q1 += dq2[0]
            sum_q2 -= dq2[0]
            dq1.append(dq2.popleft())
        else:
            sum_q1 -= dq1[0]
            sum_q2 += dq1[0]
            dq2.append(dq1.popleft())
        answer += 1
        # print(sum_q1,sum_q2, dq1, dq2)
    return answer

print(solution([3,2,7,2,], [4,6,5,1]))
print(solution([1, 2, 1, 2], 	[1, 10, 1, 2]))
print(solution([1, 1], [1,5]))