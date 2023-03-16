from collections import deque
import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    while len(scoville) != 1 and scoville[0] < K:
        l1 = heapq.heappop(scoville)
        l2 = heapq.heappop(scoville)
        
        heapq.heappush(scoville, l1+(l2*2))
        cnt += 1

    return -1 if scoville[0] < K else cnt

print(solution([1, 2, 3, 9, 10, 12], 7))