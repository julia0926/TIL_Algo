from collections import deque
#이제 이걸 pop하지 말고 인덱스로 처리하자 ! 

def solution(queue1, queue2):
    q1_start, q2_start = 0, 0
    total = len(queue1)
    sum_q1, sum_q2 = sum(queue1), sum(queue2)

    while True:
        if sum_q1 == sum_q2:
            return q1_start + q2_start
        if q1_start >= total*2 or q2_start >= total*2:
            return -1
        if sum_q1 < sum_q2:
            sum_q1 += queue2[q2_start]
            sum_q2 -= queue2[q2_start]
            queue1.append(queue2[q2_start])
            q2_start += 1 #인덱스 하나 증가시킴
        else:
            sum_q1 -= queue1[q1_start]
            sum_q2 += queue1[q1_start]
            queue2.append(queue1[q1_start])
            q1_start += 1 #인덱스 하나 증가시켜서 popleft 하는 것처럼 


print(solution([3,2,7,2,], [4,6,5,1]))
print(solution([1, 2, 1, 2], 	[1, 10, 1, 2]))
print(solution([1, 1], [1,5]))