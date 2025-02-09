from collections import deque

def solution(priorities, location):
    dq = deque()
    answer = 0
    for (idx, val) in enumerate(priorities):
        dq.append((idx, val))
    
    while True:
        val = dq.popleft()
        if any(val[1] < dqv[1] for dqv in dq): #dq의 값을 하나씪 돌면서 작은 값이 하나라도 있는지 체크 any 써서..
            dq.append(val)
        else:
            answer += 1 #없으면 실행중인 순서가 늘으니까 +1
            if val[0] == location: #찾으려는 위치 값을 찾으면
                return answer  # 바로 순서를 리턴한다.
