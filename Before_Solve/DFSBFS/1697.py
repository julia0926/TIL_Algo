from collections import deque


def bfs(n, k):
    dq = deque()
    dq.append(n)

    while dq:
        v = dq.popleft()
        if v == k:
            print(visited[k])
            break
        if v-1 >= 0 and visited[v-1] == 0:
            dq.append(v-1)
            visited[v-1] = visited[v] + 1 #방문처리 
        if v+1 <= 100000 and visited[v+1] == 0:
            dq.append(v+1)
            visited[v+1] = visited[v] + 1
        if v*2 <= 100000 and visited[v+1] == 0:
            dq.append(v*2)
            visited[v*2] = visited[v] + 1



n, k = map(int, input().split())
visited = [0] * 100001
bfs(n, k)