from heapq import heappush, heappop

def solution(k, score):
    hq = [] #명예의 전당
    answer = []
    for idx, val in enumerate(score):
        if idx < k:
            heappush(hq, val)
        else:
            if hq[0] < val:
                heappop(hq)
                heappush(hq, val)
        answer.append(hq[0])
    return answer
