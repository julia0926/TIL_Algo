#https://school.programmers.co.kr/learn/courses/30/lessons/138477
import heapq

def solution(k, score):
    answer = [] #발표점수 
    hq = [] #명예의전당
    for idx, val in enumerate(score):
        if idx < k:
            heapq.heappush(hq,val)
        else:
            if hq[0] < val: #명예의 전당 최하위 < score
                heapq.heappop(hq) #명예의전당 작은거 지우고
                heapq.heappush(hq,val) #명예의전당에 현재 score 집어넣음
        answer.append(hq[0]) #발표점수는 항상 명예의전당의 제일 작은값 넣음
        # print(answer)

    return answer

solution(3, [10, 100, 20, 150, 1, 100, 200])