# https://www.acmicpc.net/problem/1655
import heapq

n = int(input())
heap = []
for i in range(n):
    x = int(input())
    heapq.heappush(heap, x) #힙에 값을 넣고
    #중간 값을 찾아야함 
    print(heap)
    heap_len = len(heap) 
    if heap_len % 2 == 0: #짝수라면
        print(min(heap[heap_len], heap[heap_len+1]))
    else:
        print(heap[len])


