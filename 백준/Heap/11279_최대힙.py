import heapq
import sys

input = sys.stdin.readline
n = int(input())
heap = []

for _ in range(n):
    x = int(input())
    if x == 0:
        if not heap:
            print(0)
        else:
            print(-heapq.heappop(heap)) #뺄때 - 붙여서 나옴
    else:
        heapq.heappush(heap, -x) #최소힙에서 넣을때 - 붙이고