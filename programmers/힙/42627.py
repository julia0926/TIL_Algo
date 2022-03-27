# 디스크 컨트롤러 : https://programmers.co.kr/learn/courses/30/lessons/42627
import heapq as hq

'''
1. 소요시간 순으로 정렬
2. abs(시작시간 - 처음이 끝나는 시간) + 소요시간  -> 이거 3번 계산 
1 - 9 = 8 + 9 = 17 이거 
'''

def solution(jobs):
    jobs.sort(key=lambda x: x[1])
    result = []
    end_time = 0
    for start, during in jobs:
        x = abs(start - end_time) + during
        #print("endTime" , end_time)
        end_time = x + start
        result.append(x)
    return sum(result) // len(jobs)


print(solution([[0, 3], [1, 9], [2, 6]]))