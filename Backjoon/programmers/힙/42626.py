# 더 맵게 : https://programmers.co.kr/learn/courses/30/lessons/42626
import heapq as hq

level = 0
cnt = 0
def solution(scoville, K):
    hq.heapify(scoville)
    answer = 0
    while scoville[0] < K and len(scoville) >= 2:
        first = hq.heappop(scoville)
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second * 2)
        answer += 1
    if scoville[0] >= K:
        return answer
    else:
        return -1

    
print(solution([1, 2, 3, 9, 10, 12], 7))