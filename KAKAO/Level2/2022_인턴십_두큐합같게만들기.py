'''
참고하여 풀었음
값을 직접 제거하지 않고 합 값을 미리 선언하여
각 배열의 시작값을 증가시키면서 popleft 하는 효과
헷갈림 ㅜㅜ
'''

def solution(queue1, queue2):
    sum_q1, sum_q2 = sum(queue1), sum(queue2)
    result = (sum_q1 + sum_q2) // 2
    count = -1
    q1_start, q2_start, total = 0, 0, len(queue1) * 2
    #q1, q2의 길이가 둘을 합친 길이보단 작아야 하며 둘 값이 같으면 종료
    while q1_start<total and q2_start<total and sum_q1 != sum_q2:
        if sum_q1 < result:  #왼쪽 합이 더 작으면 
            sum_q1 += queue2[q2_start]
            sum_q2 -= queue2[q2_start]
            queue1.append(queue2[q2_start])
            q2_start += 1
        else: #오른쪽 합이 더 작으면 
            sum_q1 -= queue1[q1_start]
            sum_q2 += queue1[q1_start]
            queue2.append(queue1[q1_start])
            q1_start += 1
    if sum_q1 == sum_q2:
        count = q1_start + q2_start
    return count

print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
print(solution([1, 2, 1, 2], 	[1, 10, 1, 2]	))
print(solution([1,1], [1,5]))