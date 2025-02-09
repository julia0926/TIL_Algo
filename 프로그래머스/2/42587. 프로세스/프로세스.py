from collections import deque

def solution(priorities, location):
    dic = dict() #key=location, value=priority
    dq_pri = deque()
    loc_alpha = '' #찾아야할 알파벳 위치
    progress_process = [] # 실행 프로세스
    for (idx, val) in enumerate(priorities):
        alpha = chr(65+idx)
        dic[alpha] = val 
        dq_pri.append(alpha)
        if location == idx:
            loc_alpha = alpha
    
    while dq_pri:
        val = dq_pri.popleft() #1. 대기큐에서 하나 꺼낸다.
        is_progress = True
        # 2. 우선순위가 더 높은 프로세스가 있느지 비교
        for dqv in list(dq_pri):
            if dic[dqv] > dic[val]: #우선순위가 더 높은 프로세스가 있다면 
                dq_pri.append(val) #다시 큐에 넣는다.
                is_progress = False
                break
        if is_progress:
            progress_process.append(val) #실행
    
    answer = progress_process.index(loc_alpha)+1
    return answer
