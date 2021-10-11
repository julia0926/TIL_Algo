import heapq

def solution(scoville, k):
    heap = []
    # 가지고 있는 요소를 push, pop 할때마다 자동으로 정렬
    for n in scoville:
        heapq.heappush(heap, n)
    print(heap)
    answer = 0
    while heap[0] < k:
        if len(heap) == 1: return -1
        # heappop : 제일 작은 값 팝하고 반환
        heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
        answer += 1
    return answer

# -------- 테스트는 통과, 시간초과
# def solution(scoville, k):
#     heapq.heapify(scoville) #이미 리스트가 있으면 즉각 힙으로 변환됨
#     answer = 0
#     while scoville[0] < k:
#         if len(scoville) == 1: return -1
#         mix = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2) # heappop : 제일 작은 값 팝하고 반환
#         heapq.heappush(scoville, mix)
#         scoville.sort()
#         answer += 1
#     return answer


# -------- 1차 실패
# def solution(scoville, k):
#     answer = 0
#     while scoville[0] < k:
#         # 배열에 7 이상 값이 있는지
#         if len(scoville) == 1: return -1        
#         mix = scoville[0] + (scoville[1] * 2)
#         scoville.pop(0)
#         scoville.pop(0)
#         scoville.append(mix)
#         scoville.sort()
#         answer+=1
#     #     print(scoville)
#     # print(answer)
#     return answer

print(solution([9, 3, 2, 1, 12, 10], 7))