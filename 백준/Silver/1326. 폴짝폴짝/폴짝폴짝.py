import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
arr = [0] + list(map(int, input().rstrip().split()))
a, b = map(int, input().rstrip().split())
visited = [False] * (n+1)

def bfs():
    dq = deque()
    dq.append((a, 0)) #시작점, 얼마나 걸리는지
    visited[a] = True #처음 시작점은 방문처리

    while dq:
        now, time = dq.popleft()
        if now == b: #도착점에 도착했다면
            return time

        for i in range(now, n+1, arr[now]):
            if not visited[i]:
                visited[i] = True
                dq.append((i, time+1))
        
        for i in range(now, 0, -arr[now]):
            if not visited[i]:
                visited[i] = True
                dq.append((i, time+1))

    return -1

print(bfs())

