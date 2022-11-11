# 프로그래머스 스택/큐 : 기능개발
# https://programmers.co.kr/learn/courses/30/lessons/42586
from collections import deque

def solution(progresses, speeds):
    answer = []
    day = 0 #모든 작업의 날짜 (공통으로 사용하기 위함 )
    cnt = 0 #몇 개의 기능이 완료 되는지
    answer = []
    while len(progresses) != 0:
        # 55 + 8 * 5 = 35 + 55 = 100
        if progresses[0] + day * speeds[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        else: #이전 작업 일수로  or 현재 작업일수로 계산했을 때 현재 작업이 100%가 안되고 
            if cnt > 0: # 기존에 작업이 있다면 
                answer.append(cnt)
                cnt = 0
            day += 1

    answer.append(cnt)
    return answer

print(solution([93, 30, 55],[1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))