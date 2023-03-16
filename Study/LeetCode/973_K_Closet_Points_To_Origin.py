#https://leetcode.com/problems/k-closest-points-to-origin/

from heapq import heappush, heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for (x, y) in points:
            dist = x ** 2 + y ** 2
            heappush(heap, (dist, x, y))
        
        result = []

        for _ in range(k): #k번 가까운 점 목록
            (dist, x, y) = heappop(heap)
            result.append((x, y))
        return result
