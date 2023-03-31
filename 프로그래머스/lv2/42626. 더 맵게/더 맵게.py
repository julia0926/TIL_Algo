from heapq import heapify, heappop, heappush

def solution(scoville, K):
    heapify(scoville)
    count = 0
    while scoville[0] < K:
        first = heappop(scoville)
        second = heappop(scoville) * 2
        heappush(scoville, first+second)
        count += 1

        if len(scoville) == 1 and scoville[0] < K:
            return -1
    return count
