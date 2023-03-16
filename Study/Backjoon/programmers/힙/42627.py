# 디스크 컨트롤러 : https://programmers.co.kr/learn/courses/30/lessons/42627
import heapq as hq

'''
1. 소요시간 순으로 정렬
2. abs(시작시간 - 처음이 끝나는 시간) + 소요시간  -> 이거 3번 계산 
1 - 9 = 8 + 9 = 17 이거 
'''

def solution(jobs):
    answer, start = 0, 0
    jobs.sort(key=lambda x: x[1]) #소요시간 순으로 정렬
    length = len(jobs)
    while len(jobs) != 0:
        for i in range(len(jobs)):
            if jobs[i][0] <= start:
                start += jobs[i][1] #시작 시간 업데이트
                answer += start - jobs[i][0]
                print("start, answer", answer, start)
                jobs.pop(i)
                print(jobs)
                break
            if i == len(jobs) -1:
                start += 1
    return answer // length
    
    
#print(solution([[0, 3], [1, 9], [2, 6]]))
print(solution([[0, 5], [2, 10], [10000, 2]])) #6
#[[10000, 2], [0, 5], [2, 10]]