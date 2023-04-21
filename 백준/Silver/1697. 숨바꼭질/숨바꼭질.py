from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
result = []
visited = [0] * 100001

def bfs():
    dq = deque()
    dq.append(n)
    
    while dq:
        v = dq.popleft()
        if v == k:
            print(visited[v])
            break
        #elif가 안된이유 모든 경우를 다 넣어서 계산해봐야해서!
        if 0 <= v+1 <= 100000 and visited[v+1] == 0:
            visited[v+1] = visited[v]+1
            dq.append(v+1)
        if 0 <= v-1 <= 100000 and visited[v-1] == 0:
            visited[v-1] = visited[v]+1
            dq.append(v-1)
        if 0 <= v * 2 <= 100000 and visited[v*2] == 0:
            visited[v*2] = visited[v]+1
            dq.append(v*2)

bfs()
